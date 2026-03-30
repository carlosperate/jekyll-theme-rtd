/*
 * Contains features and tweaks specific for this Jekyll Read the Docs port.
 * This is so that the original theme.js and theme_extra.js files can be
 * easily compared with the upstream ones from MkDocs:
 * https://github.com/mkdocs/mkdocs/commits/master/mkdocs/themes/readthedocs
 */
(function (window, document, navigator) {
  'use strict';

  function addCodeBlockCopyButton() {
    if (navigator.clipboard) {
      /* Clipboard icon by Solar Icons, CC BY 4.0 License https://www.figma.com/community/file/1166831539721848736 */
      const iconCopy = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M16 4.00195C18.175 4.01406 19.3529 4.11051 20.1213 4.87889C21 5.75757 21 7.17179 21 10.0002V16.0002C21 18.8286 21 20.2429 20.1213 21.1215C19.2426 22.0002 17.8284 22.0002 15 22.0002H9C6.17157 22.0002 4.75736 22.0002 3.87868 21.1215C3 20.2429 3 18.8286 3 16.0002V10.0002C3 7.17179 3 5.75757 3.87868 4.87889C4.64706 4.11051 5.82497 4.01406 8 4.00195" stroke="currentColor" stroke-width="1.5"/><path d="M8 14H16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M7 10.5H17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M9 17.5H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M8 3.5C8 2.67157 8.67157 2 9.5 2H14.5C15.3284 2 16 2.67157 16 3.5V4.5C16 5.32843 15.3284 6 14.5 6H9.5C8.67157 6 8 5.32843 8 4.5V3.5Z" stroke="currentColor" stroke-width="1.5"/></svg>';
      const iconCheck = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" aria-hidden="true"><path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/></svg>';

      document.querySelectorAll('div.rst-content pre').forEach(function(pre) {
        const wrapper = document.createElement('div');
        wrapper.className = 'copy-code-wrapper';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        const btn = document.createElement('button');
        btn.className = 'copy-code-btn';
        btn.setAttribute('aria-label', 'Copy code to clipboard');
        btn.setAttribute('title', 'Copy to clipboard');
        btn.innerHTML = iconCopy;
        wrapper.appendChild(btn);
        btn.addEventListener('click', function() {
          const code = pre.querySelector('code');
          navigator.clipboard.writeText((code || pre).textContent.trimEnd()).then(function() {
            btn.innerHTML = iconCheck;
            btn.classList.add('copied');
            setTimeout(function() {
                btn.innerHTML = iconCopy;
                btn.classList.remove('copied');
            }, 2000);
          });
        });
      });
    }
  }

  window.JekyllRtd = {
    addCodeBlockCopyButton: addCodeBlockCopyButton,
  };
})(window, document, navigator);
