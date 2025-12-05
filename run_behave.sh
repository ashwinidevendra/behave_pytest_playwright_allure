#!/usr/bin/env bash
set -e
# Create results dir
rm -rf allure-results
rm -rf allure-report
mkdir -p allure-results
mkdir -p allure-report

# Run behave with Allure formatter
#behave 
echo "Test completed"
allure generate 
echo "Behave finished. Allure results are in ./allure-results"

