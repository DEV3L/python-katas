from app.model.build_status import BuildStatus


def test_build_status_init():
    expected_branch_name = 'branch_name'
    expected_number = 1
    expected_status = 'pass'
    expected_time = '1m'

    build_status = BuildStatus(
        branch_name=expected_branch_name,
        number=expected_number,
        status=expected_status,
        time=expected_time
    )

    assert expected_branch_name == build_status.branch_name
    assert expected_number == build_status.number
    assert expected_status == build_status.status
    assert expected_time == build_status.time
