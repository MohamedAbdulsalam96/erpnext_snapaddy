## snapADDY Integration

Sync leads from snapADDY to ERPNext

### Konfiguration

Please create a Role and User in ERPNext, who can only create Leads and Addresses. This user will be used for the snapADDY integration. Create an API Key and API Secret for this user.

Please configure snapADDY as follows:

- **Endpoint-URL:** https://my-erp.com/api/method/erpnext_snapaddy.api.data_quality
- **HTTP method:** POST
- **Authorization Header:** Basic AUTH_TOKEN

(The AUTH_TOKEN is created from the API Key and API Secret of the above user in base64 encoding.)

#### License

GPLv3