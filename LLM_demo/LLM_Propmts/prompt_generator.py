from langchain_core.prompts import PromptTemplate 

template = PromptTemplate(
    template = """You are a helpful Assistant.
       Explain following Topic: {topic}
       With Difficulty level : {level}
       Explaination style : {style}
       
       Instructions : 
       Explain the topic in selected difficulty level and style. 
       Provide some examples and use cases if necessar. 
       End with at least 3 quiz questions.
    """,
    input_variables = ['topic', 'level', 'style'],
    validate_template = True
)

template.save('template.json')