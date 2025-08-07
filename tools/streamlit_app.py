import requests
import streamlit as st


def make_semantic_query(query: str, limit: int = 3) -> dict | None:
    url = "http://localhost:8080/api/v1/search/semantic_query"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    payload = {"natural_query": query, "limit": limit}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error making request: {str(e)}")

        return None


def main():
    st.title("🔍 Search Amazon Products")
    st.markdown("### 📊 Using Tabular Semantic Search")
    st.markdown("### ⚡ Powered by Superlinked and MongoDB")

    st.markdown(
        "> Find products based on a product description, price, rating or other product ID/ASIN."
    )
    st.markdown(">All in a single search! ✨")
    query = st.text_input(
        "Enter your search query:",
        placeholder="e.g., books with a price lower than 100 and a rating bigger than 4",
    )

    limit = st.slider("Number of results", min_value=1, max_value=10, value=3)

    if st.button("Search"):
        if query:
            with st.spinner("Searching..."):
                results = make_semantic_query(query, limit)

            if results and "results" in results:
                st.subheader("Search Results")

                for item in results["entries"]:
                    fields = item["fields"]
                    st.markdown(f"""
                    #### ID: {item['id']}
                    - **Price:** ${fields.get('price', 'N/A')}
                    - **Rating:** ⭐ {fields.get('review_rating', 'N/A')}
                    - **Category:** {', '.join(fields.get('category', []))}
                    - **Type:** {fields.get('type', 'N/A')}
                    ---""")

        else:
            st.warning("Please enter a search query")


if __name__ == "__main__":
    main()
