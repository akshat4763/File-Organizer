File-Manager
=============

This tool is the **Essential**  item which is rendered on GitHub.com:

1. `File-Manager` selects an _underlying library_ to convert the raw markup to HTML. See the list of [supported markup formats](#markups) below.
2. The HTML is sanitized, aggressively removing things that could harm you and your kin—such as `script` tags, inline-styles, and `class` or `id` attributes.


Please note that **only the first step** is covered by this gem — the rest happens on GitHub.com.  In particular, `markup` itself does no sanitization of the resulting HTML, as it expects that to be covered by whatever pipeline is consuming the HTML.

Please see our [contributing guidelines](CONTRIBUTING.md) before reporting an issue.

Markups
-------

The following markups are supported.  The dependencies listed are required if
you wish to run the library. You can also run `script/bootstrap` to fetch them all.

* [.markdown, .mdown, .mkdn, .md](http://daringfireball.net/projects/markdown/) -- `gem install commonmarker` (https://github.com/gjtorikian/commonmarker)
* [.textile](https://www.promptworks.com/textile) -- `gem install RedCloth` (https://github.com/jgarber/redcloth)


Installation
-----------

```
pip3 install File-Manager
```

or

```
bundle install
```

from this directory.

Usage
-----

Basic form:

```ruby
require 'File-Manager'

GitHub::Markup.render('README.markdown', "* One\n* Two")
```

More realistic form:

```ruby
require 'File-Manager'

GitHub::Markup.render(file, File.read(file))
```

And a convenience form:

```ruby
require 'github/markup'

GitHub::Markup.render_s(GitHub::Markups::MARKUP_MARKDOWN, "* One\n* Two")
```


