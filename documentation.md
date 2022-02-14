# Documentation

This theme is a subtheme of [`stable9`](https://www.drupal.org/docs/8/theming-drupal-8/using-classy-as-a-base-theme).
It uses [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/) for responsiveness.

## Regions

The regions are defined in [`enccb_theme.info.yml`](enccb_theme.info.yml).

+ `secondary_menu` ("Top menu"): should contain a  [menu](https://www.drupal.org/docs/user_guide/en/menu-concept.html), which will be displayed as an inline list.
+ `header` ("Header"): should contain the `Site Branding` block, without site name or slogan.
+ `primary_menu` ("Main menu"): should contain the default `Main navigation` menu. Handle one level of submenu if `Number of levels to display` is set to `> 1` (and preferably `Expand all menu links` is checked).
+ `highlighted` ("Highlighted"): can be used to display some featured content. Goes well with "tiling" (see below). Disappear if breakpoint is `md` or lower.
+ `help` ("Help"): May contain the `Help` block and the `Status message` one.
+ `page_title` ("Page Title"): Should contain the `Page title` block.
+ `content` ("Content"): the content. Should at least contain the `Main page content` and `Tabs` blocks.
+ `footer_left` ("Footer (left column)"): Left (and smaller, since `.col-lg-4` is used) column of the footer. Can contain menus.
+ `footer_right` ("Footer (right column)"): Right (and larger, since `col-lg-8` is used) column of the footer. Can contain the `Search` block.
+ `footer` ("Footer (bottom)"): Full length region of the footer, below the two column.

## CSS

+ adds `.view-mode-[mode]` to each views
+ adds `.[field-name]` to each field (e.g., `.field-image`, `.field-tags`, ...)

## Note: tiling

To use the `.view-mode-tile` class:

+ To add a new display mode (and not mess around with the "Teaser" one), go `Admin > Structures > Display modes > View modes` and `Add new content view mode`. Name it `Tile`.
+ Then, go in `Administration > Structure > Content types` and select the kind of content you want to show with this new mode. Don't forget to got in `Custom display settings` and add this new view mode to the list of specific modes.
+ Then, it is possible to fully emulate a Bootstrap grid system: 1) use `Unformatted list`, 2) add some `col-xx` class in the `settings` (and remove the default one), and 3) in `advanced`, change `CSS class` and add `row`!
+ One can also add a custom image style in `Admin > Configuration > Media > Image Styles`. The combination `scale width 576` + `Crop 576x384` works well.

## Other tips and tricks

+ To remove author/date, go in `Admin > Structure > Content types`, edit one content (say, "article") and go in `Display settings` to uncheck `Display author and date information`.
+ If you want to have submenu, you need to set the "Number of levels to display" in the "main menu" block. Also, use the "Expand all menu links" option, so that the submenu appears on every page.
+ It seems that the only way to add a text in front of a contact form is by doing a block ([see there](https://drupal.stackexchange.com/questions/206267/how-to-add-predefined-text-to-contact-form)).

## Useful links for dev'

+ [Adding custom theme parameters](https://sarahcodes.medium.com/using-custom-theme-settings-in-templates-in-drupal-8-925391b8cff1).
+ [Another example](https://labs.tadigital.com/index.php/2019/07/03/advanced-theme-settings-in-drupal-8/) of custom parameters (with upload).
+ [A list of all the hooks](https://api.drupal.org/api/drupal/core%21core.api.php/group/hooks/9.3.x),
+ The one of [`hook_preprocess_HOOK()`](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Render%21theme.api.php/function/hook_preprocess_HOOK/9.3.x) (where `hook` is the theme name and `HOOK` is never really defined, but is related to the block name).
+ The one of [`hook_theme_suggestions_HOOK_alter()`](https://api.drupal.org/api/drupal/core!lib!Drupal!Core!Render!theme.api.php/function/hook_theme_suggestions_HOOK_alter/9.3.x)
+ [Suggestions based on region](https://www.drupal.org/forum/support/theme-development/2017-07-13/extra-template-name-suggestions-for-main-menus-based-on).
+ Get the type of node: `$variables['node']->getType()` in `THEME_preprocess_node()`.
