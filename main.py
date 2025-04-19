from dotenv import load_dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama



if __name__ == "__main__":
    print("hello langchain")

    information = """
    Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[2][3] He is of British and Pennsylvania Dutch ancestry.[4][5] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[6][7][8][a] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[15][16][17][18] Elon has a younger brother, Kimbal, a younger sister, Tosca, and four paternal half-siblings.[19][20][8][21] Musk was raised in the Anglican Church, in which he was baptized.[22][23]

The Musk family was wealthy during Elon's youth.[18] Despite both Elon and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[18] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines".[24][25] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[2]

After his parents divorced in 1980, Elon chose to live primarily with his father.[4][15] Elon later regretted his decision and became estranged from his father.[26] Elon has recounted trips to a wilderness school that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[27] In one incident, after an altercation with a fellow pupil, Elon was thrown down concrete steps and beaten severely, leading to him being hospitalized for his injuries.[28] Elon described his father berating him after he was discharged from the hospital.[28] Errol denied berating Elon and claimed, "The boy had just lost his father to suicide and Elon had called him stupid. Elon had a tendency to call people stupid. How could I possibly blame that child?"[29]

Elon was an enthusiastic reader of books, and had attributed his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[17][30] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[31] At age twelve, Elon sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.[32][33]
    """

    summary_template = """
         given the information {information} about a person from i want you to create:
         1. a short summary
         2. two interesting facts about them   
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )


    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
