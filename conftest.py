import os
import pytest
from datetime import datetime
import pytest_html




#  Configure HTML report filename

def pytest_configure(config):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(report_dir, f"report_{timestamp}.html")

    config.option.htmlpath = report_path
    config.option.self_contained_html = True



#  Screenshot on test failure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "_driver", None)
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            path = os.path.join(screenshot_dir, file_name)

            # Save screenshot
            driver.save_screenshot(path)

            # Attach screenshot to report
            extra = getattr(report, "extra", [])
            if item.config.pluginmanager.hasplugin("html"):
                extra.append(pytest_html.extras.image(path))
            report.extra = extra



#  Add test duration to table

def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Duration</th>")


def pytest_html_results_table_row(report, cells):
    if hasattr(report, "duration"):
        cells.insert(1, f"<td>{report.duration:.2f}s</td>")
    else:
        cells.insert(1, "<td>-</td>")




#  Add summary info
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><b>Project:</b> BhojDeals Automation</p>",
        "<p><b>Author:</b> Sudip Bhandari</p>"
    ])
