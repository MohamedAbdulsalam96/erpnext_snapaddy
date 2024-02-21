import contextlib
import frappe


@frappe.whitelist(methods="POST")
def data_quality(*args, **kwargs):
	frappe.log_error(title="snapADDY Data", message=frappe.form_dict)

	try:
		lead = create_lead(frappe.form_dict)
	except frappe.ValidationError as e:
		frappe.response["message"] = e.args[0]
		return
	except frappe.DuplicateEntryError as e:
		existing_lead = frappe.db.get_value(
			"Lead", {"email_id": frappe.form_dict.get("email")}
		)
		if existing_lead:
			frappe.response["callbackUrl"] = frappe.utils.get_url_to_form(
				"Lead", existing_lead
			)
		frappe.response["message"] = e.args[0]
		return

	with contextlib.suppress(frappe.ValidationError):
		create_address(frappe.form_dict, lead.name)

	frappe.response["callbackUrl"] = frappe.utils.get_url_to_form("Lead", lead.name)


def create_lead(data: dict):
	LEAD_FIELDS = {
		"email": "email_id",
		"firstName": "first_name",
		"gender": "gender",
		"lastName": "last_name",
		"mobile": "mobile_no",
		"organization": "company_name",
		"phone": "phone",
		"position": "job_title",
		"website": "website",
		"state": "state",
		"city": "city",
		"country": "country",
		"createdBy": "lead_owner",
	}

	lead = frappe.new_doc("Lead")
	for snap_field, frappe_field in LEAD_FIELDS.items():
		value = data.get(snap_field)
		if snap_field == "gender":
			value = get_gender(value)

		if snap_field == "country" and value:
			value = get_country(value)

		lead.set(frappe_field, value)

	return lead.insert()


def create_address(data: dict, lead: str):
	ADDRESS_FIELDS = {
		"state": "state",
		"city": "city",
		"country": "country",
		"street": "address_line1",
		"zip": "pincode",
	}

	address = frappe.new_doc("Address")
	for snap_field, frappe_field in ADDRESS_FIELDS.items():
		value = data.get(snap_field)
		if snap_field == "country" and value:
			value = get_country(value)

		address.set(frappe_field, value)

	address.append("links", {"link_doctype": "Lead", "link_name": lead})
	return address.insert()


def get_gender(gender: int) -> str | None:
	if gender == 0:
		return "Male"

	elif gender == 1:
		return "Female"

	return None


def get_country(code: str):
	return frappe.db.get_value("Country", {"code": code.lower()})
