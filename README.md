# Graphene (GraphQL) vs Dynamic-Rest

### Introduction

Graphql is the apparently hottest thing since sliced bread. According to the [graphQL website](https://graphql.org/ "graphQL website"), GraphQL:
- is a query language for APIs and a runtime for fulfilling those queries with your existing data.
- provides a complete and understandable description of the data in your API
- gives clients the power to ask for exactly what they need and nothing more
- makes it easier to evolve APIs over time
- and enables powerful developer tools.

This all seems great! However, this sounds a lot like [Dynamic-Rest](http://dynamic-rest.readthedocs.io/en/latest/ "Dynamic-Rest"), which is built on top of Django-Rest-Framework. I used Dynamic-Rest for over 3 years at my old company, AltSchool, and it fit our needs pretty much perfectly when I was there. Dynamic Rest:
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
git clone git@github.com:cooperjbrandon/graphene-investigation.git
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

In honor of the World Cup, the models represent a hypothetical World Cup application. Also, because a hypothetical scenario wouldn't be complete without a blog post tutorial, each User can have many blog posts or blog comments, and a blog post can have tags. Check out [models.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/models/models.py "models.py"). Alternatively, here is a visual representation of the models:
[![Graphene Investigation Models](https://raw.githubusercontent.com/cooperjbrandon/graphene-investigation/master/my_project_visualized.png "Graphene Investigation Models")](https://raw.githubusercontent.com/cooperjbrandon/graphene-investigation/master/my_project_visualized.png "Graphene Investigation Models")

You can create that image yourself by running the command
```
CMD='graph_models models -o my_project_visualized.png' make run
```

The graphene schema can be found in [grapheen/schema.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/grapheen/schema.py "here") and the graphene-relay schema can be found in [grapheen/schema_relay.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/grapheen/schema_relay.py "grapheen/schema_relay.py"). Note that the graphene and graphene-relay schema can't be run at the same time, so you'll have to comment out the appropriate lines in [project/schema.py](https://github.com/cooperjbrandon/graphene-investigation/blob/master/project/schema.py "project/schema.py").

Finally, the drest code (just views and serializers) can be found in the [drest directory](https://github.com/cooperjbrandon/graphene-investigation/tree/master/drest "drest directory") .

### Results

I'll write a much longer explanation of how to use both Graphene & Graphene-Relay and Dynamic-Rest in a separate blog post.

As an example, let's look at a fairly complex query that makes use of every model we've previously defined.

Desired outcome: We want to request the first 30 athletes along with their corresponding users. At the same time for those athletes, we want to load up their corresponding teams, coaches for that team, and corresponding users of those coaches. We also want to get each country for each team that was loaded. We also want to get all the games (through the teamGameComposition model), and corresponding referees for those games (through the refereeGameCompositionModel) and corresponding users for those referees. Finally, every time we load a user, we want to load any blog posts that they either have commented on or created themselves, as well as all the tags for those blog posts.

Yup that's a lot of information! We essentially want to load up every single model corresponding with the first 30 athletes.

This is what the query looks like in graphene:

```
{
  allAthletes(first: 30) {
    id
    height
    weight
    user {
      id
      username
      isStaff
      dateJoined
      posts {
        id
        title
        text
        postDate
        updated
        created
        tags {
          name
          updated
          created
        }
        comments {
          id
          creator {
            id
          }
          bodytext
          postDate
          updated
          created
        }
      }
    }
    team {
      ranking
      id
      coaches {
        id
        user {
          username
          isStaff
          email
          posts {
            id
            title
            text
            postDate
            updated
            created
            tags {
              name
              updated
              created
            }
            comments {
              id
              creator {
                id
              }
              bodytext
              postDate
              updated
              created
            }
          }
        }
      }
      country {
        id
        name
        population
        nationalAnthemText
      }
      teamGameCompositions {
        id
        game {
          startTime
          location
          id
          refereeGameCompositions {
            referee {
              poorEyesight
              id
              user {
                isSuperuser
                id
                username
                posts {
                  id
                  title
                  text
                  postDate
                  updated
                  created
                  tags {
                    name
                    updated
                    created
                  }
                  comments {
                    id
                    creator {
                      id
                    }
                    bodytext
                    postDate
                    updated
                    created
                  }
                }
              }
            }
            id
            position
          }
        }
        isHome
        result
      }
    }
  }
}
```
It might be a bit funky to get used to, but overall not too bad.

With relay enabled, it's overall less code on the backend. However, the request is pretty wonky in my opinion:
```
{
  allAthletes(first: 30) {
    edges {
      node {
        id
        height
        weight
        user {
          id
          username
          isStaff
          dateJoined
          posts {
            edges {
              node {
                id
                title
                text
                postDate
                updated
                created
                tags {
                  edges {
                    node {
                      name
                      updated
                      created
                    }
                  }
                }
                comments {
                  edges {
                    node {
                      id
                      creator {
                        id
                      }
                      bodytext
                      postDate
                      updated
                      created
                    }
                  }
                }
              }
            }
          }
        }
        team {
          ranking
          id
          coaches {
            edges {
              node {
                id
                favoriteStrategy
                user {
                  id
                  username
                  isStaff
                  email
                  posts {
                    edges {
                      node {
                        id
                        title
                        text
                        postDate
                        updated
                        created
                        tags {
                          edges {
                            node {
                              name
                              updated
                              created
                            }
                          }
                        }
                        comments {
                          edges {
                            node {
                              id
                              creator {
                                id
                              }
                              bodytext
                              postDate
                              updated
                              created
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
          country {
            id
            name
            population
            nationalAnthemText
          }
          teamGameCompositions {
            edges {
              node {
                id
                isHome
                result
                game {
                  startTime
                  location
                  id
                  refereeGameCompositions {
                    edges {
                      node {
                        id
                        position
                        referee {
                          poorEyesight
                          id
                          user {
                            isSuperuser
                            id
                            username
                            posts {
                              edges {
                                node {
                                  id
                                  title
                                  text
                                  postDate
                                  updated
                                  created
                                  tags {
                                    edges {
                                      node {
                                        name
                                        updated
                                        created
                                      }
                                    }
                                  }
                                  comments {
                                    edges {
                                      node {
                                        id
                                        creator {
                                          id
                                        }
                                        bodytext
                                        postDate
                                        updated
                                        created
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Finally, here is dynamic-rest's query. Note that this is just a normal rest API. So the previous two requests were POST requests with the graphql query embedded in the body of the request. For Dynamic-Rest, it's a normal GET request with query-params:
```
/api/athletes?include[]=user.posts.tags&include[]=user.posts.comments.creator.&include[]=team.coaches.user.posts.tags.&include[]=team.coaches.user.posts.comments.creator.&include[]=team.country.&include[]=team.team_game_compositions.game.referee_game_compositions.referee.user.posts.tags.&include[]=team.team_game_compositions.game.referee_game_compositions.referee.user.posts.comments.creator.&per_page=30&page=1
```
here is a more readable version:
```
/api/athletes
?include[]=user.posts.tags
&include[]=user.posts.comments.creator.
&include[]=team.coaches.user.posts.tags.
&include[]=team.coaches.user.posts.comments.creator.
&include[]=team.country.
&include[]=team.team_game_compositions.game.referee_game_compositions.referee.user.posts.tags.
&include[]=team.team_game_compositions.game.referee_game_compositions.referee.user.posts.comments.creator.
&per_page=30&page=1
```

Using `django-debug-toolbar`, graphene's response took 956 ms, and 1371 sql queries. Using relay was actually even worse: response time of 1120 ms and did 1606  sql queries. Holy crap that's bad! Dynamic-rest blew these numbers out of the water: 31 ms response time and only 24 queries.

The structure of the responses differ greatly between graphql and dynamic-rest, which probably helps explain the start different response times and number of queries. There is a lot of repeat info in graphql. See [graphene-response.json](https://github.com/cooperjbrandon/graphene-investigation/blob/master/example-responses/graphene-response.json "graphene-response.json"), [graphene-relay-response.json](https://github.com/cooperjbrandon/graphene-investigation/blob/master/example-responses/graphene-relay-response.json "graphene-relay-response.json"), and [dynamic-rest-response.json](https://github.com/cooperjbrandon/graphene-investigation/blob/master/example-responses/dynamic-rest-response.json "dynamic-rest-response.json"). I'll investigate example why Graphene is way slower in a separate blog post.

### Final Thoughts
At first glance, Dynamic-Rest is way faster, more efficient, and provides more functionality out of the box. However, this does not mean it's any better (or worse) than graphql. Although they seem similar tools, the use cases differ. GraphQL integrates super easily with apollo-client. If you are expecting your data as a graph from the backend, graphQL might be the choice for you. However, if you are using a front end ORM tool like ember-data, Dyanmic-Rest is a pretty great choice. More on this in a later post!

This README is meant as a placeholder until I can write an actual blog post about the above, along with explaining more differences between graphene and dynamic-rest such as: filtering, pagination, writes, and anything else that comes to mind.
