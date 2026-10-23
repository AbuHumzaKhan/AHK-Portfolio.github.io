# Portfolio Upgrade — Development Branch

## Scope
This branch preserves the existing `main` branch while separating the single-page portfolio into maintainable files.

## Changes in this phase
- Moved inline CSS to `assets/css/styles.css`.
- Moved inline JavaScript to `assets/js/main.js`.
- Updated `index.html` to load the external assets.
- Changed the resume URL to a web-safe forward-slash path.
- Added `rel="noopener noreferrer"` to external links opened in new tabs.
- Changed the contact form from a false success message to an honest email-client handoff. This static site does not have a message backend, so the visitor must send the prefilled email from their own email app.

## Known items still requiring content verification
- Existing project repository links did not resolve during the audit; replace them only with confirmed destinations.
- The AWS certificate record points to an asset absent from the current repository tree.
- Confirm the correct public location and resume PDF before publishing those details.
- Review internship dates, descriptions, and outcome metrics for accuracy.
- Replace or remove hard-coded GitHub counts unless verified dynamically.

## Validation required before merge
1. Confirm the page loads and browser console is clean.
2. Verify every image, certificate preview, project card, modal, theme control, and responsive layout.
3. Test the contact form's email-client handoff.
4. Verify resume download and all outbound URLs.
5. Review content and mobile layout.
6. Merge only after approval; deployment is not claimed by this branch alone.
