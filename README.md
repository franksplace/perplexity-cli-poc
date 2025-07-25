
# perplexity ai AIOps POC

## Usage

Perpelexity Pro Subscriptions and API configured.  API details at https://www.perplexity.ai/help-center/en/articles/10352995-api-settings

```
export PERPLEXITY_API_KEY=<your API key>

usage: perplexity-cli.py [-h] [--model MODEL] [--max_tokens MAX_TOKENS] [--api_key API_KEY] [--include_citations]
                         prompt output_file

Send a prompt to Perplexity AI and save output to a file.

positional arguments:
  prompt                The prompt to send to Perplexity AI (wrap in quotes)
  output_file           Output file to save the AI response

options:
  -h, --help            show this help message and exit
  --model MODEL         Model to use (default: sonar-pro)
  --max_tokens MAX_TOKENS
                        Max tokens in response (default: 1000)
  --api_key API_KEY     API key as env variable or CLI param
  --include_citations   Include citations in the output

```


