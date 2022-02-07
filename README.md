# Drupal theme `enccb_theme`

Theme for the [EuroCC NCC Belgium website](https://www.enccb.be/). Currently in development.

## Development

On your computer,

1. Create a [minimal drupal install](https://www.digitalocean.com/community/tutorials/how-to-develop-a-drupal-9-website-on-your-local-machine-using-docker-and-ddev).
2. Clone the repository in `/web/theme`.
3. Go in `Admin > Appearance` and "Install and set as default" the "ENCCB theme".
4. `ddev composer require "drupal/twig_debugger"` and `ddev composer require "drupal/admin_toolbar"`. To activate, Go in `Admin > extend` and check the corresponding checkboxes.
4. For some change, you may need to clear the cache, using the admin toolbar (or `Admin > Configuration > Development > Performances`, but it is longer).

... Have fun!

## Useful links

+ [Adding custom theme parameters](https://sarahcodes.medium.com/using-custom-theme-settings-in-templates-in-drupal-8-925391b8cff1).
+ [Another example](https://labs.tadigital.com/index.php/2019/07/03/advanced-theme-settings-in-drupal-8/) of custom parameters (with upload).
+ [A list of all the hooks](https://api.drupal.org/api/drupal/core%21core.api.php/group/hooks/9.3.x), and the one of [`hook_preprocess_HOOK()`](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Render%21theme.api.php/function/hook_preprocess_HOOK/9.3.x) (where `hook` is the theme name and `HOOK` is never really defined, but is related to the block name).
