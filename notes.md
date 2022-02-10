# Note took during dev'

+ Views can help to distinguish between tags. You can add a header (the `Global: Text area` one is fine)! Or use **taxonomy view** instead?
+ In `Admin > Structure > Content type`, you can define extra contents, with extra fields. May be useful for user stories.
+ To remove author/date, go in `Admin > Structure > Content types`, edit one content (say, "article") and go in `Display settings` to uncheck `Display author and date information`.
+ If you want to have submenu, you need to set the "Number of levels to display" in the "main menu" block. Also, use the "Expand all menu links" option, so that the submenu appears on every page.
+ It seems that the only way to add a text in front of a contact form is by doing a block ([see there](https://drupal.stackexchange.com/questions/206267/how-to-add-predefined-text-to-contact-form)).
+ Same goes for the front page, actually: [see there](https://sarahcodes.medium.com/how-to-make-a-nice-drupal-8-homepage-without-modules-or-modifying-theme-files-3ce7ce24926e).

## Tiling

+ To add a new display mode (and not mess around with the "Teaser" one), go `Admin > Structures > Display modes` and `Add new content view mode`. Then, go in `Administration > Structure > Content types` and select the kind of content you want to show as this new mode. Don't forget to got in `Customl display settings` and add this new view mode to the list of specific modes.
+ Then, it is possible to fully emulate a Bootstrap grid system: 1) use `Unformatted list`, 2) add some `col-xx` class in the `settings` (and remove the default one), and 3) in `advanced`, change `CSS class` and add `row`!
+ One can also add a custom image style in `Admin > Configuration > Media > Image Styles`. The combination `scale width 576` + `Crop 576x384` works well.
