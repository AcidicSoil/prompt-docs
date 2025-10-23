```md
<!-- $1 = Template title (e.g., "Voice Input") -->
<!-- $2 = Trigger command (e.g., "/voice-input") -->
<!-- $3 = Purpose statement (e.g., "Support interaction from voice capture and convert to structured prompts") -->
<!-- $4 = Step description (e.g., "Accept transcript text") -->
<!-- $5 = Output format description (e.g., "Cleaned command list ready to execute") -->

**Voice Input Template**

Trigger: $2

Purpose: $3

## Steps
1. $4
2. Normalize to tasks or commands for other prompts.
3. Preserve speaker intents and important entities.

## Key entities
*(e.g., speaker intent, command type, entities)*

## Expected output
$5
```
