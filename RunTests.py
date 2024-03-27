import unittest
import os
from unitTests import TestAPIEndpoints
import zipfile
from datetime import datetime
import shutil

# Define your test suite
def suite():
    suite = unittest.TestSuite()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestAPIEndpoints)
    return test_suite

# Run the tests and capture the output
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())

    # Write the results to a file
    result_file_name = 'test_results.txt'
    with open(result_file_name, 'w') as result_file:
        result_file.write('Errors:\n')
        for error in result.errors:
            result_file.write('%s\n' % error)
        result_file.write('\nFailures:\n')
        for failure in result.failures:
            result_file.write('%s\n' % failure)
        result_file.write('\nSuccesses:\n')
        result_file.write('Tests run: %s\n' % result.testsRun)
        successes = result.testsRun - len(result.failures) - len(result.errors)
        result_file.write('Successes: %s\n' % successes)

    # Create a zip file with the current date and time as the filename
    zip_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_test_results.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Zip the result file
        zipf.write(result_file_name, arcname=result_file_name)
    
    # Create 'test results' folder if it doesn't exist
    test_results_dir = 'test results'
    os.makedirs(test_results_dir, exist_ok=True)

    # Move the zip into the 'test results' folder
    shutil.move(zip_filename, os.path.join(test_results_dir, zip_filename))

    # Delete the original result file from the main folder
    os.remove(result_file_name)