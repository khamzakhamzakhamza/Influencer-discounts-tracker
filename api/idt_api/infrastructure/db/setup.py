from neo4j import GraphDatabase

def setup_constraints(driver):
    cypher_queries = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.username IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE"
    ]

    with driver.session() as session:
        for query in cypher_queries:
            session.run(query)

def setup_db(db_url: str, db_username: str, db_password: str):
    driver = GraphDatabase.driver(db_url, auth=(db_username, db_password))
    setup_constraints(driver)
    driver.close()
