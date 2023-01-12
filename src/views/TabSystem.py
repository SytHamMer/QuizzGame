from tkinter import *


class TabSystem:
    def __init__(self, tabContainer, contents, defaultTab: str):
        self.tabContainer = tabContainer
        """ 
        Enable to know which tab is associatied to a contentDefiner.
        """
        self.contents = contents
        self.activedTabSlug = defaultTab
        self.activedTab = None
        self.setTab(self.activedTabSlug)

    def setTab(self, slug) -> None:
        """Update the current Tab.

        Args:
            slug (string): Slug of the new tab.
        """
        contentDefiner = self.contents[slug]

        if (contentDefiner == None):
            raise Exception('Error 404: tab not found.')

        for widget in self.tabContainer.winfo_children():
            widget.destroy()

        self.activedTab = contentDefiner(self.tabContainer)
        self.activedTabSlug = slug

    def getActivedTab(self):
        return self.activedTab

    def getActivedTabSlug(self) -> str:
        return self.activedTabSlug
