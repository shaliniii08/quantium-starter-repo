import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_header_present():
    layout = app.layout
    assert "Pink Morsels Sales Visualiser" in str(layout)


def test_graph_present():
    layout = app.layout
    assert "sales-line-chart" in str(layout)


def test_region_picker_present():
    layout = app.layout
    assert "region-filter" in str(layout)


