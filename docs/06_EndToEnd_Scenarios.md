# End to End Scenarios
Scenario 01
Read a SharePoint page by path
Expected behavior
1. Orchestrator chooses OneDrive SharePoint Worker
2. Worker validates path
3. Worker returns content
4. Run log records the call and the result

Scenario 02
Create a Jira issue
Expected behavior
1. Orchestrator requires project selection if not provided
2. Orchestrator requests the user to choose a project
3. After selection, orchestrator calls Jira Worker
4. Worker returns issue key and summary
5. Run log records every step

Scenario 03
Post to Teams
Expected behavior
1. Orchestrator requires team and channel selection
2. Orchestrator requests selection when missing
3. Teams Worker confirms post target and returns message id
