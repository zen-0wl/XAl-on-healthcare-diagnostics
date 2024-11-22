{%- extends 'full.tpl' -%}

{%- block body -%}
{{ super() }}
{%- for cell in nb.cells if 'tags' in cell.metadata and 'export' in cell.metadata.tags -%}
{{ cell.source }}
{%- endfor -%}
{%- endblock body -%}