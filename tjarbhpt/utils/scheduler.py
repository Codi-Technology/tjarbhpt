import frappe

def custom_send():
	enabled_reports = frappe.get_all(
		"Auto Email Report", filters={"enabled": 1, "frequency": "6 PM"}
	)

	for report in enabled_reports:
		auto_email_report = frappe.get_doc("Auto Email Report", report.name)
		try:
			auto_email_report.run_method("send")
		except Exception as e:
			auto_email_report.log_error(f"Failed to send {auto_email_report.name} Auto Email Report")