from main import app


def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")

    assert header.text == "Impact of Pink Morsel Price Increase on Sales"


def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element("#sales-chart") is not None


def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element("#region-filter") is not None