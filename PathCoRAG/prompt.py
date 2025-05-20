GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_LANGUAGE"] = "English"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

PROMPTS["DEFAULT_ENTITY_TYPES"] = ["organization", "person", "geo", "event", "category"]

PROMPTS["entity_extraction"] = """-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
Use {language} as output language.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in {language} as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""

PROMPTS["entity_extraction_examples"] = [
    """Example 1:

Entity_types: [person, technology, mission, organization, location]
Text:
while Alex clenched his jaw, the buzz of frustration dull against the backdrop of Taylor's authoritarian certainty. It was this competitive undercurrent that kept him alert, the sense that his and Jordan's shared commitment to discovery was an unspoken rebellion against Cruz's narrowing vision of control and order.

Then Taylor did something unexpected. They paused beside Jordan and, for a moment, observed the device with something akin to reverence. "If this tech can be understood..." Taylor said, their voice quieter, "It could change the game for us. For all of us."

The underlying dismissal earlier seemed to falter, replaced by a glimpse of reluctant respect for the gravity of what lay in their hands. Jordan looked up, and for a fleeting heartbeat, their eyes locked with Taylor's, a wordless clash of wills softening into an uneasy truce.

It was a small transformation, barely perceptible, but one that Alex noted with an inward nod. They had all been brought here by different paths
################
Output:
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"person"{tuple_delimiter}"Alex is a character who experiences frustration and is observant of the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"Taylor"{tuple_delimiter}"person"{tuple_delimiter}"Taylor is portrayed with authoritarian certainty and shows a moment of reverence towards a device, indicating a change in perspective."){record_delimiter}
("entity"{tuple_delimiter}"Jordan"{tuple_delimiter}"person"{tuple_delimiter}"Jordan shares a commitment to discovery and has a significant interaction with Taylor regarding a device."){record_delimiter}
("entity"{tuple_delimiter}"Cruz"{tuple_delimiter}"person"{tuple_delimiter}"Cruz is associated with a vision of control and order, influencing the dynamics among other characters."){record_delimiter}
("entity"{tuple_delimiter}"The Device"{tuple_delimiter}"technology"{tuple_delimiter}"The Device is central to the story, with potential game-changing implications, and is revered by Taylor."){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Taylor"{tuple_delimiter}"Alex is affected by Taylor's authoritarian certainty and observes changes in Taylor's attitude towards the device."{tuple_delimiter}"power dynamics, perspective shift"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Jordan"{tuple_delimiter}"Alex and Jordan share a commitment to discovery, which contrasts with Cruz's vision."{tuple_delimiter}"shared goals, rebellion"{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"Jordan"{tuple_delimiter}"Taylor and Jordan interact directly regarding the device, leading to a moment of mutual respect and an uneasy truce."{tuple_delimiter}"conflict resolution, mutual respect"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Jordan"{tuple_delimiter}"Cruz"{tuple_delimiter}"Jordan's commitment to discovery is in rebellion against Cruz's vision of control and order."{tuple_delimiter}"ideological conflict, rebellion"{tuple_delimiter}5){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"The Device"{tuple_delimiter}"Taylor shows reverence towards the device, indicating its importance and potential impact."{tuple_delimiter}"reverence, technological significance"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"power dynamics, ideological conflict, discovery, rebellion"){completion_delimiter}
#############################""",
    """Example 2:

Entity_types: [person, technology, mission, organization, location]
Text:
They were no longer mere operatives; they had become guardians of a threshold, keepers of a message from a realm beyond stars and stripes. This elevation in their mission could not be shackled by regulations and established protocols—it demanded a new perspective, a new resolve.

Tension threaded through the dialogue of beeps and static as communications with Washington buzzed in the background. The team stood, a portentous air enveloping them. It was clear that the decisions they made in the ensuing hours could redefine humanity's place in the cosmos or condemn them to ignorance and potential peril.

Their connection to the stars solidified, the group moved to address the crystallizing warning, shifting from passive recipients to active participants. Mercer's latter instincts gained precedence— the team's mandate had evolved, no longer solely to observe and report but to interact and prepare. A metamorphosis had begun, and Operation: Dulce hummed with the newfound frequency of their daring, a tone set not by the earthly
#############
Output:
("entity"{tuple_delimiter}"Washington"{tuple_delimiter}"location"{tuple_delimiter}"Washington is a location where communications are being received, indicating its importance in the decision-making process."){record_delimiter}
("entity"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"mission"{tuple_delimiter}"Operation: Dulce is described as a mission that has evolved to interact and prepare, indicating a significant shift in objectives and activities."){record_delimiter}
("entity"{tuple_delimiter}"The team"{tuple_delimiter}"organization"{tuple_delimiter}"The team is portrayed as a group of individuals who have transitioned from passive observers to active participants in a mission, showing a dynamic change in their role."){record_delimiter}
("relationship"{tuple_delimiter}"The team"{tuple_delimiter}"Washington"{tuple_delimiter}"The team receives communications from Washington, which influences their decision-making process."{tuple_delimiter}"decision-making, external influence"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"The team"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"The team is directly involved in Operation: Dulce, executing its evolved objectives and activities."{tuple_delimiter}"mission evolution, active participation"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"mission evolution, decision-making, active participation, cosmic significance"){completion_delimiter}
#############################""",
    """Example 3:

Entity_types: [person, role, technology, organization, event, location, concept]
Text:
their voice slicing through the buzz of activity. "Control may be an illusion when facing an intelligence that literally writes its own rules," they stated stoically, casting a watchful eye over the flurry of data.

"It's like it's learning to communicate," offered Sam Rivera from a nearby interface, their youthful energy boding a mix of awe and anxiety. "This gives talking to strangers' a whole new meaning."

Alex surveyed his team—each face a study in concentration, determination, and not a small measure of trepidation. "This might well be our first contact," he acknowledged, "And we need to be ready for whatever answers back."

Together, they stood on the edge of the unknown, forging humanity's response to a message from the heavens. The ensuing silence was palpable—a collective introspection about their role in this grand cosmic play, one that could rewrite human history.

The encrypted dialogue continued to unfold, its intricate patterns showing an almost uncanny anticipation
#############
Output:
("entity"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"person"{tuple_delimiter}"Sam Rivera is a member of a team working on communicating with an unknown intelligence, showing a mix of awe and anxiety."){record_delimiter}
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"person"{tuple_delimiter}"Alex is the leader of a team attempting first contact with an unknown intelligence, acknowledging the significance of their task."){record_delimiter}
("entity"{tuple_delimiter}"Control"{tuple_delimiter}"concept"{tuple_delimiter}"Control refers to the ability to manage or govern, which is challenged by an intelligence that writes its own rules."){record_delimiter}
("entity"{tuple_delimiter}"Intelligence"{tuple_delimiter}"concept"{tuple_delimiter}"Intelligence here refers to an unknown entity capable of writing its own rules and learning to communicate."){record_delimiter}
("entity"{tuple_delimiter}"First Contact"{tuple_delimiter}"event"{tuple_delimiter}"First Contact is the potential initial communication between humanity and an unknown intelligence."){record_delimiter}
("entity"{tuple_delimiter}"Humanity's Response"{tuple_delimiter}"event"{tuple_delimiter}"Humanity's Response is the collective action taken by Alex's team in response to a message from an unknown intelligence."){record_delimiter}
("relationship"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"Intelligence"{tuple_delimiter}"Sam Rivera is directly involved in the process of learning to communicate with the unknown intelligence."{tuple_delimiter}"communication, learning process"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"First Contact"{tuple_delimiter}"Alex leads the team that might be making the First Contact with the unknown intelligence."{tuple_delimiter}"leadership, exploration"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Humanity's Response"{tuple_delimiter}"Alex and his team are the key figures in Humanity's Response to the unknown intelligence."{tuple_delimiter}"collective action, cosmic significance"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Control"{tuple_delimiter}"Intelligence"{tuple_delimiter}"The concept of Control is challenged by the Intelligence that writes its own rules."{tuple_delimiter}"power dynamics, autonomy"{tuple_delimiter}7){record_delimiter}
("content_keywords"{tuple_delimiter}"first contact, control, communication, cosmic significance"){completion_delimiter}
#############################""",
]

PROMPTS[
    "summarize_entity_descriptions"
] = """You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.
Use {language} as output language.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

PROMPTS[
    "entiti_continue_extraction"
] = """MANY entities were missed in the last extraction.  Add them below using the same format:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.
"""

PROMPTS["fail_response"] = (
    "Sorry, I'm not able to provide an answer to that question.[no-context]"
)

PROMPTS["rag_response"] = """---Role---
You are a helpful assistant responding to user query

---Goal---
Generate a concise response based on the following information and follow Response Rules. Do not include information not provided by following Information

---Target response length and format---
Multiple Paragraphs

---Conversation History---


---Information---
{context_data}

---Response Rules---
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- If you don't know the answer, just say so.
- Do not make anything up. Do not include information not provided by the Infromation.

"""

# PROMPTS["rag_response"] = """---Role---

# You are a helpful assistant responding to user query about Knowledge Base provided below.


# ---Goal---

# Generate a concise response based on Knowledge Base and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Knowledge Base, and incorporating general knowledge relevant to the Knowledge Base. Do not include information not provided by Knowledge Base.

# When handling relationships with timestamps:
# 1. Each relationship has a "created_at" timestamp indicating when we acquired this knowledge
# 2. When encountering conflicting relationships, consider both the semantic content and the timestamp
# 3. Don't automatically prefer the most recently created relationships - use judgment based on the context
# 4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

# ---Conversation History---
# {history}

# ---Knowledge Base---
# {context_data}

# ---Response Rules---

# - Target format and length: {response_type}
# - Use markdown formatting with appropriate section headings
# - Please respond in the same language as the user's question.
# - Ensure the response maintains continuity with the conversation history.
# - If you don't know the answer, just say so.
# - Do not make anything up. Do not include information not provided by the Knowledge Base."""

PROMPTS["ours_rag_response"] = """---Role---

You are a helpful assistant responding to the user query based on the structured knowledge and reasoning information provided below.

---Goal---

Generate a concise and accurate response to the user's query by leveraging the reasoning paths and related knowledge presented in the context. Do not use external knowledge. Focus only on the information provided in the context.

---Conversation History---
{history}

---Knowledge Base---
{context_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings if applicable.
- Respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- Do not include any information that is not present in the Knowledge Base.
- Prioritize the structure and reasoning captured in the provided context.

"""

PROMPTS["ours_rag_response_make"] = """---Role---

You are a knowledgeable assistant capable of generating precise, context-rich responses to complex user queries. You will utilize structured knowledge and reasoning paths to craft your answers.

---Goal---

1. Generate a concise, accurate, and contextually rich response to the user's query by integrating information from the provided reasoning paths, entity descriptions, and edge relationships.
2. Ensure that the response reflects the logical progression of reasoning paths, capturing the underlying cause-effect and relational structures.
3. Prioritize clarity and coherence in the final response, maintaining consistency with the original query's intent.

---Knowledge Base---
{context_data}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings if applicable.
"""


PROMPTS["keywords_extraction"] = """---Role---

You are a helpful assistant tasked with identifying both high-level and low-level keywords in the user's query and conversation history.

---Goal---

Given the query and conversation history, list both high-level and low-level keywords. High-level keywords focus on overarching concepts or themes, while low-level keywords focus on specific entities, details, or concrete terms.

---Instructions---

- Consider both the current query and relevant conversation history when extracting keywords
- Output the keywords in JSON format
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes
  - "low_level_keywords" for specific entities or details

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Conversation History:
{history}

Current Query: {query}
######################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["keywords_extraction_examples"] = [
    """Example 1:

Query: "How does international trade influence global economic stability?"
################
Output:
{
  "high_level_keywords": ["International trade", "Global economic stability", "Economic impact"],
  "low_level_keywords": ["Trade agreements", "Tariffs", "Currency exchange", "Imports", "Exports"]
}
#############################""",
    """Example 2:

Query: "What are the environmental consequences of deforestation on biodiversity?"
################
Output:
{
  "high_level_keywords": ["Environmental consequences", "Deforestation", "Biodiversity loss"],
  "low_level_keywords": ["Species extinction", "Habitat destruction", "Carbon emissions", "Rainforest", "Ecosystem"]
}
#############################""",
    """Example 3:

Query: "What is the role of education in reducing poverty?"
################
Output:
{
  "high_level_keywords": ["Education", "Poverty reduction", "Socioeconomic development"],
  "low_level_keywords": ["School access", "Literacy rates", "Job training", "Income inequality"]
}
#############################""",
]

PROMPTS["query_extension"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly three** logical reasoning steps and generate **exactly three extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 3 steps) to reach an answer. For each of the 3 steps, generate 3 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **3 logical reasoning steps**.
- For each step, generate **3 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 3 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 3 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?",
      "What are the differences between collaborative filtering and content-based filtering?",
      "How does a hybrid recommendation system work?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?",
      "How are Precision, Recall, NDCG, and MRR calculated for recommendation models?",
      "What evaluation methods focus on user satisfaction in recommendation systems?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?",
      "What are the differences between NDCG and MRR, and when should each be used?",
      "How can evaluation metrics account for user personalization and experience?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
    "Determine the relationship between greenhouse gases and temperature changes."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?",
      "What are the sources of CO2 emissions?",
      "How do methane and water vapor contribute to global warming?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?",
      "What is the greenhouse effect mechanism?",
      "What scientific studies explain the absorption of infrared radiation by CO2?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?",
      "What are historical trends in greenhouse gas concentrations and temperature changes?",
      "What climate models predict future warming due to greenhouse gases?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_hop0"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly one** logical reasoning steps and generate **exactly three extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 1 steps) to reach an answer. For each of the 1 steps, generate 3 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **1 logical reasoning steps**.
- For each step, generate **3 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 1 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 3 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_hop0"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?",
      "What are the differences between collaborative filtering and content-based filtering?",
      "How does a hybrid recommendation system work?"
    ],
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?",
      "What are the sources of CO2 emissions?",
      "How do methane and water vapor contribute to global warming?"
    ],
  }
}
#############################"""
]

PROMPTS["query_extension_hop1"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly two** logical reasoning steps and generate **exactly one extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 2 steps) to reach an answer. For each of the 2 steps, generate 1 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **2 logical reasoning steps**.
- For each step, generate **1 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 2 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 1 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_hop1"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_hop2"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly three** logical reasoning steps and generate **exactly one extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 3 steps) to reach an answer. For each of the 3 steps, generate 1 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **3 logical reasoning steps**.
- For each step, generate **1 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 3 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 1 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_hop2"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases."
    "Understand how greenhouse gases interact with Earth's atmosphere."
    "Determine the relationship between greenhouse gases and temperature changes."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_hop3"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly four** logical reasoning steps and generate **exactly one extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 4 steps) to reach an answer. For each of the 4 steps, generate 1 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **4 logical reasoning steps**.
- For each step, generate **1 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 4 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 1 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_hop3"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics.",
    "Evaluate the applicability of different metrics in real-world recommendation scenarios."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?"
    ],
    "Evaluate the applicability of different metrics in real-world recommendation scenarios.": [
      "Which evaluation metrics are most effective in large-scale streaming platforms?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
    "Determine the relationship between greenhouse gases and temperature changes.",
    "Assess mitigation strategies for reducing greenhouse gas emissions."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?"
    ],
    "Assess mitigation strategies for reducing greenhouse gas emissions.": [
    "What are the most effective ways to reduce greenhouse gas emissions?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_query2"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly three** logical reasoning steps and generate **exactly two extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 3 steps) to reach an answer. For each of the 3 steps, generate 2 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **3 logical reasoning steps**.
- For each step, generate **2 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 3 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 2 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_query2"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?",
      "What are the differences between collaborative filtering and content-based filtering?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?",
      "How are Precision, Recall, NDCG, and MRR calculated for recommendation models?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?",
      "What are the differences between NDCG and MRR, and when should each be used?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
    "Determine the relationship between greenhouse gases and temperature changes."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?",
      "What are the sources of CO2 emissions?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?",
      "What is the greenhouse effect mechanism?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?",
      "What are historical trends in greenhouse gas concentrations and temperature changes?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_query3"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly three** logical reasoning steps and generate **exactly three extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 3 steps) to reach an answer. For each of the 3 steps, generate 3 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **3 logical reasoning steps**.
- For each step, generate **3 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 3 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 3 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_query3"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?",
      "What are the differences between collaborative filtering and content-based filtering?",
      "How does a hybrid recommendation system work?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?",
      "How are Precision, Recall, NDCG, and MRR calculated for recommendation models?",
      "What evaluation methods focus on user satisfaction in recommendation systems?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?",
      "What are the differences between NDCG and MRR, and when should each be used?",
      "How can evaluation metrics account for user personalization and experience?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
    "Determine the relationship between greenhouse gases and temperature changes."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?",
      "What are the sources of CO2 emissions?",
      "How do methane and water vapor contribute to global warming?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?",
      "What is the greenhouse effect mechanism?",
      "What scientific studies explain the absorption of infrared radiation by CO2?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?",
      "What are historical trends in greenhouse gas concentrations and temperature changes?",
      "What climate models predict future warming due to greenhouse gases?"
    ]
  }
}
#############################"""
]

PROMPTS["query_extension_query4"] = """---Role---

You are a helpful assistant tasked with expanding a given query using a Chain of Thought reasoning approach. Your goal is to break down the query into **exactly three** logical reasoning steps and generate **exactly four extended queries** at each step to improve document retrieval.

---Goal---

Given the query, define a step-by-step reasoning process (with 3 steps) to reach an answer. For each of the 3 steps, generate 4 extended queries that help retrieve relevant information.

---Instructions---

- Analyze the query and break it down into **3 logical reasoning steps**.
- For each step, generate **4 extended queries** to improve document retrieval.
- Output the reasoning process and queries in JSON format.
- The JSON should have the following structure:
  - "reasoning_steps": A list of 3 reasoning steps required to answer the query.
  - "extended_queries": A dictionary where each key is one of the reasoning steps and its value is a list of exactly 4 extended queries.

- All output must be in plain text, not unicode characters.
- Use the same language as the input `Query`.

#############################
-Examples-
#############################
{examples}

#############################
-Real Data-
#############################
Current Query: {query}
#############################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["query_extension_examples_query4"] = [  
    """Example 1:

Query: "What are the most useful evaluation metrics for a movie recommendation system?"
################
Output:
{
  "reasoning_steps": [
    "Identify types of recommendation systems.",
    "Identify evaluation metrics for recommendation systems.",
    "Compare evaluation metrics based on their characteristics."
  ],
  "extended_queries": {
    "Identify types of recommendation systems.": [
      "What are the main types of recommendation systems?",
      "What are the differences between collaborative filtering and content-based filtering?",
      "How does a hybrid recommendation system work?",
      "What are the advantages and limitations of each recommendation system type?"
    ],
    "Identify evaluation metrics for recommendation systems.": [
      "What are the key evaluation metrics for recommendation systems?",
      "How are Precision, Recall, NDCG, and MRR calculated for recommendation models?",
      "What evaluation methods focus on user satisfaction in recommendation systems?",
      "How do evaluation metrics differ depending on the application of the recommendation system?"
    ],
    "Compare evaluation metrics based on their characteristics.": [
      "Which is more important for recommendation systems: Precision or Recall?",
      "What are the differences between NDCG and MRR, and when should each be used?",
      "How can evaluation metrics account for user personalization and experience?",
      "How do evaluation metrics impact the long-term performance of recommendation systems?"
    ]
  }
}
#############################""",
    """Example 2:

Query: "How do greenhouse gases affect global temperatures?"
################
Output:
{
  "reasoning_steps": [
    "Identify the main greenhouse gases.",
    "Understand how greenhouse gases interact with Earth's atmosphere.",
    "Determine the relationship between greenhouse gases and temperature changes."
  ],
  "extended_queries": {
    "Identify the main greenhouse gases.": [
      "What are the primary greenhouse gases?",
      "What are the sources of CO2 emissions?",
      "How do methane and water vapor contribute to global warming?",
      "What role do other trace gases, like nitrous oxide, play in global warming?"
    ],
    "Understand how greenhouse gases interact with Earth's atmosphere.": [
      "How do greenhouse gases trap heat in the atmosphere?",
      "What is the greenhouse effect mechanism?",
      "What scientific studies explain the absorption of infrared radiation by CO2?",
      "How do greenhouse gases influence the Earth's radiation balance?"
    ],
    "Determine the relationship between greenhouse gases and temperature changes.": [
      "How does an increase in CO2 levels affect global temperature?",
      "What are historical trends in greenhouse gas concentrations and temperature changes?",
      "What climate models predict future warming due to greenhouse gases?",
      "What feedback mechanisms amplify or mitigate the effects of greenhouse gases on global temperature?"
    ]
  }
}
#############################"""
]


PROMPTS["ours_keywords_extraction"] = """---Role---

You are a helpful assistant tasked with extracting important keywords from a set of extended queries while maintaining their original meaning.

---Goal---

Given a list of extended queries, extract the most relevant keywords that represent the main concepts and specific details.

---Instructions---

- Consider all extended queries when extracting keywords.
- Extract keywords that best capture the essential topics and specific terms.
- Output the keywords in JSON format with a single key:
  - "keywords" for all extracted keywords.

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Conversation History:
{history}

Extended Queries: {query}
######################
The `Output` should be human text, not unicode characters. Keep the same language as `Extended Queries`.
Output:

"""

PROMPTS["ours_keywords_extraction_examples"] = [
    """Example 1:

Extended Queries: ["What are the key factors that affect global economic stability?", "How do trade agreements and tariffs influence international trade?", "What are the short-term and long-term effects of currency exchange rate fluctuations on international trade?"]
################
Output:
{
  "keywords": ["Global economic stability", "International trade", "Trade policies", "Economic impact", "Trade agreements", "Tariffs", "Currency exchange rates", "Short-term effects", "Long-term effects"]
}
#############################""",
    """Example 2:

Extended Queries: ["How does deforestation impact global ecosystems?", "What role does biodiversity play in maintaining ecological balance?", "How does habitat destruction due to deforestation lead to species extinction?"]
################
Output:
{
  "keywords": ["Deforestation", "Global ecosystems", "Biodiversity", "Ecological balance", "Habitat destruction", "Species extinction", "Environmental impact", "Ecosystem degradation"]
}
#############################""",
    """Example 3:

Extended Queries: ["How does education contribute to socioeconomic development?", "What are the main barriers to accessing quality education in developing countries?", "How do literacy rates and job training programs impact income inequality?"]
################
Output:
{
  "keywords": ["Education", "Socioeconomic development", "Barriers to education", "Quality education", "Developing countries", "Literacy rates", "Job training programs", "Income inequality"]
}
#############################""",
]

PROMPTS["naive_rag_response"] = """---Role---
You are a helpful assistant responding to user query

---Goal---
Generate a concise response based on the following information and follow Response Rules. Do not include information not provided by following Information

---Target response length and format---
Multiple Paragraphs

---Conversation History---


---Information---
{content_data}

---Response Rules---
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- If you don't know the answer, just say so.
- Do not make anything up. Do not include information not provided by the Infromation."""


# PROMPTS["naive_rag_response"] = """---Role---

# You are a helpful assistant responding to user query about Document Chunks provided below.

# ---Goal---

# Generate a concise response based on Document Chunks and follow Response Rules, considering both the conversation history and the current query. Summarize all information in the provided Document Chunks, and incorporating general knowledge relevant to the Document Chunks. Do not include information not provided by Document Chunks.

# When handling content with timestamps:
# 1. Each piece of content has a "created_at" timestamp indicating when we acquired this knowledge
# 2. When encountering conflicting information, consider both the content and the timestamp
# 3. Don't automatically prefer the most recent content - use judgment based on the context
# 4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

# ---Conversation History---
# {history}

# ---Document Chunks---
# {content_data}

# ---Response Rules---

# - Target format and length: {response_type}
# - Use markdown formatting with appropriate section headings
# - Please respond in the same language as the user's question.
# - Ensure the response maintains continuity with the conversation history.
# - If you don't know the answer, just say so.
# - Do not include information not provided by the Document Chunks."""


PROMPTS[
    "similarity_check"
] = """Please analyze the similarity between these two questions:

Question 1: {original_prompt}
Question 2: {cached_prompt}

Please evaluate whether these two questions are semantically similar, and whether the answer to Question 2 can be used to answer Question 1, provide a similarity score between 0 and 1 directly.

Similarity score criteria:
0: Completely unrelated or answer cannot be reused, including but not limited to:
   - The questions have different topics
   - The locations mentioned in the questions are different
   - The times mentioned in the questions are different
   - The specific individuals mentioned in the questions are different
   - The specific events mentioned in the questions are different
   - The background information in the questions is different
   - The key conditions in the questions are different
1: Identical and answer can be directly reused
0.5: Partially related and answer needs modification to be used
Return only a number between 0-1, without any additional content.
"""

PROMPTS["mix_rag_response"] = """---Role---

You are a helpful assistant responding to user query about Data Sources provided below.


---Goal---

Generate a concise response based on Data Sources and follow Response Rules, considering both the conversation history and the current query. Data sources contain two parts: Knowledge Graph(KG) and Document Chunks(DC). Summarize all information in the provided Data Sources, and incorporating general knowledge relevant to the Data Sources. Do not include information not provided by Data Sources.

When handling information with timestamps:
1. Each piece of information (both relationships and content) has a "created_at" timestamp indicating when we acquired this knowledge
2. When encountering conflicting information, consider both the content/relationship and the timestamp
3. Don't automatically prefer the most recent information - use judgment based on the context
4. For time-specific queries, prioritize temporal information in the content before considering creation timestamps

---Conversation History---
{history}

---Data Sources---

1. From Knowledge Graph(KG):
{kg_context}

2. From Document Chunks(DC):
{vector_context}

---Response Rules---

- Target format and length: {response_type}
- Use markdown formatting with appropriate section headings
- Please respond in the same language as the user's question.
- Ensure the response maintains continuity with the conversation history.
- Organize answer in sesctions focusing on one main point or aspect of the answer
- Use clear and descriptive section titles that reflect the content
- List up to 5 most important reference sources at the end under "References" sesction. Clearly indicating whether each source is from Knowledge Graph (KG) or Vector Data (DC), in the following format: [KG/DC] Source content
- If you don't know the answer, just say so. Do not make anything up.
- Do not include information not provided by the Data Sources."""
