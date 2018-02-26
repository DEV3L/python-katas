from app.actions.fetch_build_status import FetchBuildStatus

def test_fetch_build_status_init(browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_console_url = f'http://jenkins-ci.route53.osstage.net:8080/view/OnShift-OnShift/job/OnShift-OnShift/job/' \
                        f'{expected_branch_name}/{expected_build_number}/console'

    fetch_build_status = FetchBuildStatus(browser_client, expected_branch_name, expected_build_number)

    assert expected_branch_name == fetch_build_status.branch_name
    assert expected_build_number == fetch_build_status.build_number
    assert expected_console_url == fetch_build_status.console_url
