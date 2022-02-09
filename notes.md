# Note took during dev'

+ Views can help to distinguish between tags. You can add a header (the `Global: Text area` one is fine)! Or use **taxonomy view** instead?
+ In `Admin > Structure > Content type`, you can define extra contents, with extra fields. May be useful for user stories.
+ If you want to have submenu, you need to set the "Number of levels to display" in the "main menu" block. Also, use the "Expand all menu links" option, so that the submenu appears on every page.
+ Get the type of node: `$variables['node']->getType()` in `THEME_preprocess_node()`.
