#!/usr/bin/env python3
"""
Entry point for the refactoring agent.
"""
import logging
from agent import run_agent

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )

def main():
    setup_logging()
    logging.info("Starting refactoring agent...")
    run_agent()

if __name__ == "__main__":
    main() 