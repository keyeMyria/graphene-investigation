# Graphene (GraphQL) vs Dynamic-Rest

### Introduction

Graphql is the apparently hottest thing since sliced bread. According to the [graphQL website](https://graphql.org/ "graphQL website"), GraphQL:
- is a query language for APIs and a runtime for fulfilling those queries with your existing data.
- provides a complete and understandable description of the data in your API
- gives clients the power to ask for exactly what they need and nothing more
- makes it easier to evolve APIs over time
- and enables powerful developer tools.

This all sounds great! However, this sounds a lot like [Dynamic-Rest](http://dynamic-rest.readthedocs.io/en/latest/ "Dynamic-Rest"), which is built on top of Django-Rest-Framework. I used Dynamic-Rest for over 3 years at my old company, AltSchool, and it fit our needs pretty much perfectly when I was there. Dynamic Rest:
- empowers simple RESTful APIs with the flexibility of a graph query language
- offers the following features on top of the standard Django Rest Framework kit
  - Linked relationships
  - Sideloaded relationships
  - Embedded relationships
  - Inclusions
  - Exclusions
  - Filtering
  - Sorting
  - Directory panel for your Browsable API
  - Optimizations

 Sounds pretty similar to graphql! This leads me to the question: what's the difference? Is one better than the other?
 
### Setup
1. 
```
brew install pipenv
```
2. 
```
git clone <insert_repo_url_here>
```
3. 
```
cd graphene-investigation
```
4. 
```
pipenv install
```
5. Create a postgres DB locally and name it `graphene_investigation`.
6.  Apply migrations to the db
```
make migrate
```
7.  Populate the db with data
```
CMD=refresh_db make run
```
8.  Start the server
```
make start
```

### Walk through of project

This project has 3 apps, `models` (which just contains the models that will be consumed by the other 2 apps), `grapheen` (which runs both graphene and relay), and `drest` (which runs dynamic rest).

In honor of the World Cup, the models represent a hypothetical World Cup application. Also, because a hypothetical scenario wouldn't be complete without this, each User can have many blog posts or blog comments, and a blog post can have tags. Check out [models.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/models/models.py "models.py"). Alternatively, here is a visual representation of the models:
[![Graphene Investigation Models](https://raw.githubusercontent.com/cooperjbrandon/graphene-investigation/master/my_project_visualized.png "Graphene Investigation Models")](https://raw.githubusercontent.com/cooperjbrandon/graphene-investigation/master/my_project_visualized.png "Graphene Investigation Models")

You can create that image yourself by running the command
```
CMD='graph_models models -o my_project_visualized.png' make run
```

The graphene schema can be found in [grapheen/schema.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/grapheen/schema.py "here") and the graphene-relay schema can be found in [grapheen/schema_relay.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/grapheen/schema_relay.py "grapheen/schema_relay.py"). Note that the graphene and graphene-relay schema can't be run at the same time, so you'll have to comment out the appropriate lines in [project/schema.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/project/schema.py "project/schema.py").

Finally, the drest code (just views and serializers) can be found in the [drest directory](https://github.com/cooperjbrandon/graphene-investigation/tree/master/drest "drest directory") .

### Results

I'll write a much longer explanation of how to use both Graphene & Graphene-Relay and Dynamic-Rest in a separate blog post.

Cutting to the chase: **Dynamic-Rest is way faster, more efficient, and easier to use right of the box.**

First, let's look at basic 
