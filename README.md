# Drupal theme `enccb_theme`

Theme for the [EuroCC NCC Belgium website](https://www.enccb.be/). Currently in development.

The templates originate from the `stable` core theme. The goal is to touch as small of them as possible.

## Development

On your computer,

1. Create a [minimal drupal install](https://www.digitalocean.com/community/tutorials/how-to-develop-a-drupal-9-website-on-your-local-machine-using-docker-and-ddev).
2. Clone the repository in `/web/theme`.
3. Go in `Admin > Appearance` and "Install and set as default" the "ENCCB theme".
4. `ddev composer require "drupal/twig_debugger"` and `ddev composer require "drupal/admin_toolbar"`. To activate, Go in `Admin > extend` and check the corresponding checkboxes.
5. Enable theme `stable9` with `drush theme:enable stable9`.
6. For some change, you may need to clear the cache, using the admin toolbar (or `Admin > Configuration > Development > Performances`, but it is longer).
7. To compile the SCSS template, you need to install a SCSS compiler, i.e. `pip3 install --user libsass`. Then, compile it with `make`.

... Have fun and [check the documentation](documentation.md) first.

