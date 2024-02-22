## snapADDY Integration

Sync leads from snapADDY to ERPNext

This app provides an endpoint for the [snapADDY Data Quality webhook](https://developers.snapaddy.com/dataquality-webhook-api/guides/getting-started). It enables your ERPNext instance to receive data from snapADDY and create new leads in ERPNext based on the received data.

### Configuration

Please create a User in ERPNext that will be used for the snapADDY integration. The user's roles should be configured in a way that it can **only** create Leads and Addresses. Create an API Key and API Secret for this user.

Please configure snapADDY as follows:

- **Endpoint-URL:** https://MY-ERP.COM/api/method/erpnext_snapaddy.api.data_quality

    > Replace `MY-ERP.COM` with your ERPNext domain.

- **HTTP method:** POST
- **Authorization Header:** Token API_KEY:API_SECRET

    > Replace `API_KEY` and `API_SECRET` with the API Key and API Secret of the user you created in ERPNext.

#### Disclaimer

This app is not affiliated with snapADDY. It is a community contribution and is not officially supported by snapADDY.

#### License

GPLv3