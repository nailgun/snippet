{{ type }}	m_{{ name }};

{% if prefix -%}
const {{ type }}& get{{ name[0]|upper }}{{ name[1:] }}();
{%- else -%}
const {{ type }}& {{ name }}();
{%- endif %}{% if setter %}
void set{{ name[0]|upper }}{{ name[1:] }}(const {{ type }}& {{ name }}) const;
{%- endif %}

{{ inline }}{% if prefix -%}
const {{ type }}& get{{ name[0]|upper }}{{ name[1:] }}() {
{%- else -%}
const {{ type }}& {{ name }}() {
{%- endif %}
	return m_{{ name }};
}{% if setter %}

{{ inline }}void set{{ name[0]|upper }}{{ name[1:] }}(const {{ type }}& {{ name }}) const {
	m_{{ name }} = {{ name }};
}
{%- endif %}

