def chain_of_thought_questions():
    print("Let's create your job search headline!")
    job_title = input("1. What is your current or target job title? ").strip()
    skills = input("2. List your top 3-5 skills or tools (comma separated): ").strip()
    industry = input("3. What industry or role do you want to target? ").strip()
    strength = input("4. What is your unique strength or career highlight? ").strip()
    impact = input("5. What impact do you want to make in your next role? ").strip()
    
    return job_title, skills, industry, strength, impact

def create_headline(job_title, skills, industry, strength, impact):
    # Basic headline template
    headline = (
        f"{job_title} | Skilled in {skills} | "
        f"{strength} | Driving {impact} in {industry}"
    )
    return headline

def reflexive_prompting(headline):
    print("\nGenerated Headline:")
    print(headline)
    print("\nDoes this headline clearly represent you? (yes/no)")
    feedback = input().strip().lower()
    if feedback == "no":
        print("\nLet's refine it! What would you like to improve?")
        improvement = input("Your feedback: ").strip()
        print("\nGreat! Consider revising your headline to include:", improvement)
    else:
        print("\nAwesome! Your headline is ready to go!")

def main():
    job_title, skills, industry, strength, impact = chain_of_thought_questions()
    headline = create_headline(job_title, skills, industry, strength, impact)
    reflexive_prompting(headline)

if __name__ == "__main__":
    main()
