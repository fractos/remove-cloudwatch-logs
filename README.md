# remove-cloudwatch-logs

Remove prefixed CloudWatch log streams from a named log group after a certain timestamp, optionally missing a specific stream.

## Environment Variables

| Name | Description | Default |
| - |- | - |
| DEBUG | Switch on debug logging | False |
| LOG_GROUP_NAME | Name of the Log Group to enumerate | |
| LOG_STREAM_NAME_PREFIX | Prefix of the Log Stream to consider for removal | |
| KEEP | Full ID of the Log Stream to keep if considered | |
| AFTER | Timestamp in %Y-%m-%d %H:%M:%S format to remove items if they are NEWER than | |
| DRY_RUN | Just show what you'd do, don't actually remove | False |


This will also need AWS credentials and region (AWS_DEFAULT_REGION) piped in as environment variables.
