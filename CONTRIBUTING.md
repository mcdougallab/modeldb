# Thank you for your interest in contributing to this project!
We want ModelDB to help as many people as possible and to be implemented in a way that allows as many
people as possible to contribute.

As you contribute, be sure to engage with the community with respect.

## Ways to contribute
There are many ways to contribute, not all of which require writing code. They include:
- Submitting issues to suggest new features or report bugs.
- Submitting pull requests to add new features linked to an issue.
- Providing constructive feedback on issues or pull requests.

All nontrivial pull requests should have an associated issue.

## A few basic groundrules:
- All code will be reviewed by the core developers before acceptance.
- Be curteous with all your posts here (no rude comments in the code, in the issues, pull requests, the wiki, etc).
  Harassment of any kind is against our community values and will not be tolerated.

## Development priorities include:
- Accessibility (e.g. screen readers)
- Analytics
- Ease of use
- Ease of contributing to the code base
- Mobile device support
- Respecting user privacy
- Security

Additionally, as of July 2020, a number of core features are still in development; see the issues tab of the repository.

## Consistent look and feel
It is important to have a consistent look-and-feel for both the code base and the website. As such:
### Python
- Code should be formatted using [black](https://github.com/psf/black). This ensures that it will meet the 
  [PEP 8](https://www.python.org/dev/peps/pep-0008/) style.
- Use `f`-strings instead of `.format` or `%`
- Loop over items, not over indices
### JavaScript
- Use `() => {}` instead of anonymous `function` definitions
- Loop over items, not over indices.
### HTML
- Use HTML for structure; use CSS for styling.
- Use centralized css and js files when practical.
### Website
- Prefer meaningful URIs over query arguments; e.g. prefer `/87284` to `?id=87284`
- Tables should generally be made searchable and sortable with bootstrapTable
- Use consistent styling where possible, avoid repeats so can stay consistent in future
- Attempting to access an internal page without authorization should generally take you to the login page
- Changes must be reasonable on both mobile and desktop environments. Dropdown menus may be a practical alternative to tabs on mobile.


Failure of existing code to follow these guidelines does not mean that future exceptions will be allowed. 
Changes to bring existing code into compliance are generally encouraged.

## Licensing
By contributing code to this repository, you are agreeing to freely share your code with no licensing restrictions.
Only submit code that you write.
In particular, note that this means GPL-licensed code cannot be accepted.

If you feel that your code needs to introduce a dependency on an external tool, please discuss this in the
corresponding issue with the core developers prior to submitting a pull request.

## Miscellaneous notes
- Code that modifies the database will be more heavily reviewed than code that just reads the database. In particular, make sure the database can only be modified by a logged-in user with the appropriate permissions.

## Finally

Note: this document is fair-game for issues and pull requests. How can we improve this?
