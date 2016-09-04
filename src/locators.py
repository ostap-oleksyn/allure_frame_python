class HomePageLoc:
    _page = "Home Page"

    SEARCH_FIELD = ["Search field", ".//*[@id='lst-ib']", _page]
    RESULT_LINK = ["Result link field", "(.//*[@class='rc'])[?]/h3/a", _page]
