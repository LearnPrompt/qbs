"""Replay the frozen debugging artifact, checking both red and green states."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent / 'debugging'
for version, code, expected_failures in [('original', 'original_listing.py', 5), ('fixed', 'listing.py', 0)]:
    with tempfile.TemporaryDirectory(prefix='qbs-debug-replay-') as tmp:
        shutil.copyfile(ROOT / code, Path(tmp) / 'listing.py')
        shutil.copyfile(ROOT / 'test_listing.py', Path(tmp) / 'test_listing.py')
        run = subprocess.run([sys.executable, '-m', 'unittest', '-v', 'test_listing'], cwd=tmp,
                             text=True, capture_output=True)
        output = run.stdout + run.stderr
        correct = ('Ran 8 tests' in output and
                   ((run.returncode == 0 and '\nOK\n' in output) if not expected_failures else
                    (run.returncode == 1 and f'FAILED (failures={expected_failures})' in output)))
        print(f'{version}: {"PASS" if correct else "FAIL"} expected failures={expected_failures}')
        if not correct:
            print(output)
            sys.exit(1)
