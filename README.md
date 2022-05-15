# Sensitive At-Rest Data Scanner

#### Scan directories, exports, and backups for sensitive data (like PII and API keys) with Nightfall's data loss prevention (DLP) APIs. Discover what lives at-rest in your data silos.

This service uses Nightfall's [data loss prevention (DLP) APIs](https://nightfall.ai/developer-platform) to scan a folder/directory, backup, or export and sends the results to a supported Nightfall alert platform as specified in your policy configured in the Nightfall console. 

For example, you can scan a backup of your Salesforce instance to detect sensitive data in Salesforce. Salesforce houses high volumes of customer information, support tickets, quotes and files, synced emails, tasks & notes, and much more. This service will (1) send Salesforce backup data to Nightfall to be scanned, (2) send an email or slack alert with a link to the sensitive findings. This output provides a comprehensive report/audit of the sensitive data at-rest in your Salesforce tenant. The same premise extends to any service that allows you to generate a backup or export.

If you'd like a more detailed tutorial or walk-through of how this service works, we recommend reviewing our [file scanner tutorial](https://github.com/nightfallai/file-scanner-tutorial), as the components are largely the same.

## Prerequisites

* Nightfall account - [sign up](https://app.nightfall.ai/sign-up) for free if you don't have an account
* If you are scanning a cloud backup or export, you'll need admin access to the data silos you wish to scan, in order to create a backup or export

## Usage

1. Create a cloud backup/export of the systems you wish to scan. Download the backup and extract it locally. We've compiled instructions for a handful of popular cloud apps below.

- [Salesforce](https://help.salesforce.com/s/articleView?id=sf.admin_exportdata.htm&type=5)
- [Jira](https://confluence.atlassian.com/adminjiraserver/backing-up-data-938847673.html)
- [Confluence](https://confluence.atlassian.com/doc/manually-backing-up-the-site-152405.html)
- [Asana](https://asana.com/guide/help/faq/security#gl-full-org-export)
- [HubSpot](https://knowledge.hubspot.com/account/export-your-content-and-data)
- [ServiceNow](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/export-sets/concept/c_ExportSets.html)
- [ClickUp](https://docs.clickup.com/en/articles/1907587-data-portability-export-your-workspace-s-data)
- [Notion](https://www.notion.so/help/back-up-your-data)
- [Coda](https://help.coda.io/en/articles/1222787-how-can-i-export-data-from-coda)
- [Monday.com](https://support.monday.com/hc/en-us/articles/360002543719-How-to-export-your-entire-account-s-data)
- [Linear](https://linear.app/docs/google-sheets)

2. Install dependencies. Add the `-U` flag to ensure you're using the latest versions of these packages.

```bash
pip install -r requirements.txt
```

3. Set your environment variables: your Nightfall API key and your Nightfall policy UUID, and the path to your extracted directory/export/backup that you want to crawl.

```bash
export NIGHTFALL_API_KEY=<your_key_here>
export NIGHTFALL_POLICY_UUID=<your_uuid_here>
export SCAN_DIRECTORY_PATH='SCAN_DIRECTORY_PATH'
```

4. Run your scan.

```python
python scanner.py
```

5. Check the alert platform you configured in your Nightfall policy (email, slack, webhook, etc). Results will include the following:

* Upload ID provided by Nightfall
* An incrementing index
* Timestamp
* Filepath
* Characters before the sensitive finding (for context)
* Sensitive finding itself
* Characters after the sensitive finding (for context)
* Confidence level of the detection
* Byte range location (character indicies) of the sensitive finding in its parent file
* Corresponding detection rules that flagged the sensitive finding
