#!/usr/bin/env python3

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict
import numpy as np

# Parse the ID document data
def parse_id_data():
    """Parse the ID document data into a structured format"""

    # Raw data from the document
    data_text = """ID Type	Name	Country
citizen-card	Citizen	Canada, Portugal
commercial-license	Commercial Drivers License	United States, United Kingdom
drivers-license	Drivers License	Afghanistan, Albania, Algeria, American Samoa, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahamas (the), Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Bermuda, Bhutan, Bolivia (Plurinational State of), Botswana, Brazil, Brunei Darussalam, Bulgaria, Burkina Faso, Burundi, Cambodia, Cameroon, Canada, Cayman Islands (the), Chad, Chili, China, Colombia, Congo (the Democratic Republic of the), Costa Rica, Côte d'Ivoire, Croatia, Cyprus, Czech Republic, Denmark, Dominica, Dominican Republic, El Salvador, Estonia, Fiji, Finland, France, Georgia, Germany, Ghana, Greece, Grenada, Guam, Guatemala, Guernsey, Guinea, Guyana, Haiti, Honduras, Hong Kong, Hungary, Iceland, India, Indonesia, Ireland, Isle of Man, Israel, Italy, Jamaica, Jersey, Jordan, Korea (the Republic of), Kuwait, Latvia, Lebanon, Libya, Liechtenstein, Lithuania, Luxembourg, Malawi, Malaysia, Maldives, Malta, Mauritius, Mexico, Micronesia (Federated States of), Moldova (the Republic of), Mongolia, Montenegro, Morocco, Mozambique, Myanmar, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger (the), Nigeria, Northern Mariana Islands (the), Norway, Oman, Pakistan, Palestine (State of), Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Puerto Rico, Qatar, Republic of Kosovo, Republic of North Macedonia, Romania, Russian Federation, Rwanda, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, South Africa, Spain, Sri Lanka, Sudan (the), Sweden, Switzerland, Syrian Arab Republic, Thailand, Togo, Trinidad and Tobago, Tunisia, Turkey, Turks and Caicos Islands (the), Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Venezuela, Vietnam, Virgin Islands (British), Virgin Islands (U.S.), Zambia, Zimbabwe
drivers-license-permit	Drivers License Permit	Australia, Canada, Ireland, New Zealand, Qatar, United Kingdom, United States
employment	Employment Card	United States
global-entry	Global Entry Card	United States
handgun	Handgun	Canada, New Zealand, Puerto Rico, United States
health-insurance	Health Insurance Card	Canada, Germany
identification	Identification Card	Afghanistan, Albania, American Samoa, Angola, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia (Plurinational State of), Bosnia and Herzegovina, Botswana, Brazil, Brunei Darussalam, Bulgaria, Burkina Faso, Cabo Verde, Cameroon, Canada, Chad, Chile, China, Colombia, Congo (the Democratic Republic of the), Costa Rica, Côte d'Ivoire, Croatia, Cuba, Curaçao, Cyprus, Czech Republic, Dominican Republic, Ecuador, El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini, Ethiopia, Finland, France, Gambia (the), Georgia, Germany, Ghana, Gibraltar, Greece, Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Honduras, Hong Kong, Hungary, India, Indonesia, Iraq, Ireland, Italy, Jamaica, Jordan, Kazakhstan, Kenya, Kuwait, Kyrgyzstan, Lao People's Democratic Republic (the), Latvia, Lebanon, Lesotho, Liechtenstein, Lithuania, Luxembourg, Malawi, Malaysia, Maldives, Malta, Mauritania, Mauritius, Mexico, Moldova (the Republic of), Monaco, Mongolia, Montenegro, Morocco, Mozambique, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Nigeria, Norway, Pakistan, Palau, Palestine (State of), Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Puerto Rico, Qatar, Republic of Kosovo, Republic of North Macedonia, Romania, Rwanda, Saint Lucia, Saint Vincent and the Grenadines, Senegal, Serbia, Singapore, Sint Maarten (Dutch part), Slovakia, Slovenia, Somalia, South Africa, South Sudan, Spain, Sri Lanka, Suriname, Sweden, Switzerland, Tajikistan, Tanzania (United Republic of), Thailand, Togo, Trinidad and Tobago, Turkey, Uganda, United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Venezuela, Vietnam, Zambia, Zimbabwe
indian	Indian Status Card	Canada, United States
matrícula consular	Matrícula Consular Card	Brazil, Mexico
nexus	Nexus Card	United States
passport	Passport	Afghanistan, Albania, Algeria, Andorra, Angola, Anguilla, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahamas (the), Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bermuda, Bhutan, Bolivia (Plurinational State of), Bosnia and Herzegovina, Botswana, Brazil, Brunei Darussalam, Bulgaria, Burkina Faso, Burundi, Cabo Verde, Cameroon, Canada, Cayman Islands (the), Chad, Chile, China, Colombia, Congo (the), Congo (the Democratic Republic of the), Costa Rica, Côte d'Ivoire, Croatia, Cuba, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic (the), Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Finland, France, Gabon, Germany, Ghana, Greece, Grenada, Guatemala, Guernsey, Guinea, Guyana, Haiti, Honduras, Hong Kong, Hungary, Iceland, India, Indonesia, Iran (Islamic Republic of), Iraq, Ireland, Isle of Man, Israel, Italy, Jamaica, Japan, Jersey, Jordan, Kazakhstan, Kenya, Kiribati, Korea (the Republic of), Kuwait, Kyrgyzstan, Lao People's Democratic Republic (the), Latvia, Lebanon, Lesotho, Liberia, Libya, Lithuania, Luxembourg, Macao, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands (the), Mauritania, Mauritius, Mexico, Micronesia (Federated States of), Moldova (the Republic of), Mongolia, Montenegro, Morocco, Mozambique, Myanmar, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger (the), Nigeria, Norway, Oman, Pakistan, Palau, Palestine (State of), Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Qatar, Republic of Kosovo, Republic of North Macedonia, Romania, Russian Federation, Rwanda, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Samoa, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Singapore, Slovakia, Slovenia, Somalia, South Africa, Spain, Sri Lanka, Sudan (the), Suriname, Sweden, Switzerland, Syrian Arab Republic, Tajikistan, Tanzania (United Republic of), Thailand, Togo, Tonga, Trinidad and Tobago, Tunisia, Turkey, Turkmenistan, Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Vanuatu, Venezuela, Vietnam, Yemen, Zambia, Zimbabwe
passport-card	Passport Card	Ukraine, United States
residence	Residence Permit	Andorra, Austria, Azerbaijan, Belgium, Bolivia (Plurinational State of), Bulgaria, Canada, Colombia, Costa Rica, Cyprus, Czech Republic, Denmark, Dominican Republic, El Salvador, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Korea (the Republic of), Latvia, Lithuania, Malta, Mexico, Montenegro, Netherlands, Norway, Oman, Panama, Peru, Poland, Portugal, Qatar, Republic of Kosovo, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, Switzerland, Taiwan, Turkey, Ukraine, United Arab Emirates, United Kingdom, United States, Vietnam
visa	Visa	Bangladesh, Colombia, Costa Rica, Dominican Republic (the), Peru, Singapore, United States"""

    # Parse the data
    country_to_ids = defaultdict(list)
    id_type_colors = {}

    # Color scheme for different ID types
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
              '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
              '#F8C471', '#82E0AA', '#F1948A', '#85C1E9']

    lines = data_text.strip().split('\n')[1:]  # Skip header

    for i, line in enumerate(lines):
        parts = line.split('\t')
        if len(parts) >= 3:
            id_type = parts[0]
            id_name = parts[1]
            countries_str = parts[2]

            # Assign color to ID type
            id_type_colors[id_type] = colors[i % len(colors)]

            # Parse countries
            countries = [c.strip() for c in countries_str.split(',')]
            for country in countries:
                # Clean up country names
                country = country.replace('(the)', '').replace('(State of)', '').strip()
                country_to_ids[country].append(id_type)

    return country_to_ids, id_type_colors

def normalize_country_names(country_to_ids):
    """Normalize country names to match plotly's country data"""

    # Country name mappings for plotly compatibility
    name_mapping = {
        'United States': 'United States of America',
        'United Kingdom': 'United Kingdom',
        'Russian Federation': 'Russia',
        'Korea Republic of': 'South Korea',
        'Iran Islamic Republic of': 'Iran',
        'Venezuela': 'Venezuela',
        'Bolivia Plurinational State of': 'Bolivia',
        'Moldova Republic of': 'Moldova',
        'Tanzania United Republic of': 'Tanzania',
        'Congo Democratic Republic of': 'Democratic Republic of the Congo',
        'Congo': 'Republic of the Congo',
        'Lao People\'s Democratic Republic': 'Laos',
        'Syrian Arab Republic': 'Syria',
        'Dominican Republic': 'Dominican Republic',
        'Côte d\'Ivoire': 'Ivory Coast',
        'Gambia': 'Gambia',
        'Niger': 'Niger',
        'Sudan': 'Sudan',
        'Bahamas': 'Bahamas',
        'Republic of North Macedonia': 'North Macedonia',
        'Republic of Kosovo': 'Kosovo'
    }

    normalized = {}
    for country, ids in country_to_ids.items():
        normalized_name = name_mapping.get(country, country)
        normalized[normalized_name] = ids

    return normalized

def create_world_map(country_to_ids, id_type_colors):
    """Create an interactive world map showing countries and their ID types"""

    # Normalize country names
    country_to_ids = normalize_country_names(country_to_ids)

    # Create a list for the map data
    countries = []
    id_counts = []
    id_types_text = []
    primary_colors = []

    for country, id_list in country_to_ids.items():
        countries.append(country)
        id_counts.append(len(id_list))
        id_types_text.append('<br>'.join(id_list))
        # Use the color of the first ID type as primary color
        primary_colors.append(id_type_colors.get(id_list[0], '#888888'))

    # Create the choropleth map
    fig = go.Figure(data=go.Choropleth(
        locations=countries,
        z=id_counts,
        locationmode='country names',
        colorscale='Viridis',
        hovertemplate='<b>%{location}</b><br>' +
                      'Number of ID Types: %{z}<br>' +
                      'ID Types:<br>%{customdata}<extra></extra>',
        customdata=id_types_text,
        colorbar=dict(
            title="Number of ID Types"
        )
    ))

    fig.update_layout(
        title={
            'text': 'World Map: ID Document Types by Country',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
        width=1200,
        height=700
    )

    return fig

def create_id_type_summary(country_to_ids, id_type_colors):
    """Create a summary chart of ID types and country counts"""

    id_type_counts = defaultdict(int)
    for country, id_list in country_to_ids.items():
        for id_type in id_list:
            id_type_counts[id_type] += 1

    # Sort by count
    sorted_items = sorted(id_type_counts.items(), key=lambda x: x[1], reverse=True)

    id_types = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    colors = [id_type_colors.get(id_type, '#888888') for id_type in id_types]

    fig = go.Figure(data=go.Bar(
        x=counts,
        y=id_types,
        orientation='h',
        marker=dict(color=colors),
        hovertemplate='<b>%{y}</b><br>Countries: %{x}<extra></extra>'
    ))

    fig.update_layout(
        title={
            'text': 'Number of Countries by ID Document Type',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title='Number of Countries',
        yaxis_title='ID Document Type',
        height=600,
        margin=dict(l=200)
    )

    return fig

def main():
    """Main function to create and display the maps"""

    print("Parsing ID document data...")
    country_to_ids, id_type_colors = parse_id_data()

    print(f"Found {len(country_to_ids)} unique countries/territories")
    print(f"Found {len(id_type_colors)} different ID types")

    # Create the world map
    print("Creating world map...")
    world_map = create_world_map(country_to_ids, id_type_colors)

    # Create the summary chart
    #print("Creating summary chart...")
    #summary_chart = create_id_type_summary(country_to_ids, id_type_colors)

    # Display the maps
    world_map.show()
    world_map.to_html('vouched-id-worldmap.html')
    #summary_chart.show()

    # Print some statistics
    print("\n--- Statistics ---")
    print(f"Total unique countries/territories: {len(country_to_ids)}")
    print(f"Total ID document types: {len(id_type_colors)}")

    # Countries with most ID types
    top_countries = sorted(country_to_ids.items(), key=lambda x: len(x[1]), reverse=True)[:10]
    print("\nTop 10 countries with most ID types:")
    for country, ids in top_countries:
        print(f"  {country}: {len(ids)} types")

    # ID types by frequency
    id_frequency = defaultdict(int)
    for ids in country_to_ids.values():
        for id_type in ids:
            id_frequency[id_type] += 1

    print("\nMost common ID types:")
    for id_type, count in sorted(id_frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"  {id_type}: {count} countries")
    

if __name__ == "__main__":
    main()
