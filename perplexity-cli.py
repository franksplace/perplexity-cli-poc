#!/usr/bin/env python3

import os
import argparse
import requests
import sys

def query_perplexity(prompt, api_key, model="sonar-pro", max_tokens=1000):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Error communicating with Perplexity API: {e}")
        sys.exit(1)

def format_citations(citations):
    if not citations:
        return ""
    lines = ["\nCitations:"]
    for idx, url in enumerate(citations, 1):
        lines.append(f"[{idx}] {url}")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to Perplexity AI and save output to a file.")
    parser.add_argument("prompt", help="The prompt to send to Perplexity AI (wrap in quotes)")
    parser.add_argument("output_file", help="Output file to save the AI response")
    parser.add_argument("--model", default="sonar-pro", help="Model to use (default: sonar-pro)")
    parser.add_argument("--max_tokens", type=int, default=1000, help="Max tokens in response (default: 1000)")
    parser.add_argument("--api_key", default=os.getenv("PERPLEXITY_API_KEY"), help="API key as env variable or CLI param")
    parser.add_argument("--include_citations", action="store_true", help="Include citations in the output")
    args = parser.parse_args()

    if not args.api_key:
        print("Error: API key required. Set PERPLEXITY_API_KEY or use --api_key")
        sys.exit(1)

    response = query_perplexity(args.prompt, args.api_key, args.model, args.max_tokens)
    
    message = response["choices"][0]["message"]["content"]
    citations = response.get("citations")

    output = message
    if args.include_citations and citations:
        output += format_citations(citations)
    
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Response saved to {args.output_file}")

if __name__ == "__main__":
    main()

