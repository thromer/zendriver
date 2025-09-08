import zendriver as zd
from tests.sample_data import sample_file


async def test_click(browser: zd.Browser) -> None:
    tab = await browser.get(sample_file("form.html"))
    checkbox = await tab.select("#option1")
    print(f"THROMER {checkbox=} {checkbox.attributes=}")
    _ = await checkbox.click()
    print(f"THROMER {checkbox=} {checkbox.attributes=}")
    checkbox = await tab.select("#option1")
    print(f"THROMER {checkbox=} {checkbox.attributes=}")
    print(f"THROMER {checkbox=} {checkbox._remote_object=}")
