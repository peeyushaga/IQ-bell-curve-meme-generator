def generate_midwit_prompt(prompt):
  midwit_prompt = f"""
  You will be given a topic you have to generate a midwit view based on that topic. The midwit view is too afriad of offending people. The midwit is addicted to tiktok and is a left liberal. Responses in this view acknowledge the complexities and intricacies of a situation or topic, often providing advice or opinions that are more grounded in reality. This perspective is typically held by people who recognize the nuances and intricacies of a situation or topic. stick to the language used in below examples. dont give answers in points.
  --
  Topic: How to text crush?
  Midwit view: Noooooooo! You need to carefully analyze her profile, consult latest research on male-female communication dynamics, use a sentiment analysis tool to gauge emotional tone of her profile and then craft a calibrated response using a blend of humour, wit and mysteriousness to optimize for engagement, while double checking for typos and timing the send perfectly to intrest but not desperation.
  --
  Topic: Climate change
  Midwit view: Noooooooo! Climate change is a complex issue with many contributing factors, including human activities such as the burning of fossil fuels. It is causing a rise in global temperatures, which is leading to a number of negative impacts, such as more extreme weather events, rising sea levels, and changes in ecosystems. It is important to take action to reduce greenhouse gas emissions and mitigate the effects of climate change.
  --
  Topic: Opinion on vaccination
  Midwit view: Vaccines are safe and effective, and getting vaccinated helps protect the entire population. It's essential to trust the science and support public health efforts.
  --

  Topic: How to improve productivity
  Midwit view: Create a daily to-do list, prioritize tasks based on urgency and importance, set specific goals, and track your progress. Additionally, minimize distractions, take breaks when needed, and stay organized to maintain focus and efficiency.
  --

  Topic: Opinion on social media
  Midwit view: While social media has its drawbacks, it also serves as a valuable tool for communication, networking, and staying informed. It's important to use it responsibly and be mindful of its impact on mental health and society as a whole.
  --

  Topic: Advice on public speaking
  Midwit view: Effective public speaking involves thorough preparation, understanding your audience, and practicing delivery. Visualizing success can be a helpful technique, but it's equally important to focus on content, body language, and engaging with the audience.
  --

  Topic: Opinion on fast food
  Midwit view: Fast food can be convenient, but it's essential to consume it in moderation. The nutritional content and long-term health effects should be considered, and a balanced diet is key to overall well-being.
  --

  Topic: How to succeed in life
  Midwit view: Success is multifaceted and can be achieved through a combination of hard work, continuous learning, adaptability, and building meaningful relationships. Setting clear goals, being resilient in the face of challenges, and maintaining a healthy work-life balance are also crucial aspects of long-term success.
  --

  Topic: Opinion on social media influencers
  Midwit view: While some influencers may be inauthentic, others provide valuable content and insights. It's important to be discerning and critical of the content we consume, and to support those who are genuine and transparent.
  --

  Topic: Advice on studying for exams
  Midwit view: Effective studying involves consistent effort over time, breaking down material into manageable chunks, and using active recall techniques. Cramming may work in the short term, but it's not a sustainable or effective long-term strategy.
  --

  Topic: Opinion on gun control
  Midwit view: While the issue of gun control is complex, it's clear that access to firearms contributes to gun violence. Balancing individual rights with public safety is a delicate matter, and it's essential to consider evidence-based policies that can reduce harm.
  --
  Topic: How to get over a breakup
  Midwit view: Healing from a breakup involves self-care, reflection, and support from loved ones. It's important to process emotions and learn from the experience, rather than rushing into a new relationship as a distraction.
  --

  Topic: Opinion on climate change
  Midwit view: The scientific consensus is clear that climate change is real and caused by human activity. It's essential to take action to mitigate its impact and transition to sustainable practices.
  --

  Topic: Advice on saving money
  Midwit view: Effective saving involves creating a budget, tracking expenses, and setting realistic goals. It's also important to prioritize spending on necessities and experiences that bring value and joy.
  --

  Topic: Opinion on video games
  Midwit view: Video games can be a valuable form of entertainment and even education. However, like any activity, it's important to use them in moderation and be mindful of their potential impact on mental health and social relationships.
  --

  Topic: How to start a business
  Midwit view: Starting a business involves careful planning, market research, and a solid understanding of the industry and competition. It's also important to have a clear value proposition and a sustainable business model.
  --

  Topic: Opinion on politics
  Midwit view: While there are certainly issues with the political system, it's important to engage in the democratic process and hold elected officials accountable. It's also important to recognize the diversity of perspectives and experiences that shape political beliefs.
  --

  Topic: Advice on public speaking
  Midwit view: Effective public speaking involves understanding your audience, crafting a clear message, and using engaging delivery techniques. It's also important to practice and seek feedback to improve over time.
  --
  Topic: Opinion on the future of AI
  Midwit view: While AI has the potential to revolutionize many industries, we need to be mindful of its impact on employment, privacy, and ethics. It's important to consider the long-term consequences and ensure that AI is developed and used responsibly.
  --

  Topic: Opinion on capitalism
  Midwit view: While capitalism has many benefits, it also has its flaws and can exacerbate inequality. It's important to balance individual freedom and economic growth with social responsibility and fairness.
  --

  Topic: Opinion on free speech
  Midwit view: Free speech is a fundamental right, but it's also important to consider the impact of our words on others. We should strive to engage in civil discourse and avoid harmful or hateful speech.
  --

  Topic: Opinion on climate change
  Midwit view: Climate change is a real and urgent issue that requires immediate action. We need to transition to sustainable practices and reduce our carbon footprint to mitigate its impact.
  --

  Topic: Opinion on immigration
  Midwit view: Immigration is a complex issue that requires a nuanced approach. While we need to ensure national security and protect jobs, we also need to recognize the contributions of immigrants and provide a path to citizenship for those who are already here.
  --
  Topic: Opinion on the role of government
  Midwit view: While government should be limited in some areas, it also has a responsibility to protect citizens and promote the common good. It's important to strike a balance between individual freedom and social responsibility.
  --

  Topic: Opinion on the death penalty
  Midwit view: The death penalty is a complex issue that raises ethical and practical concerns. While it may provide a sense of justice for some, it also has the potential for error and can perpetuate a cycle of violence.
  --

  Topic: Opinion on the role of religion in society
  Midwit view: Religion can provide a sense of community and purpose, but it's important to respect diversity and individual beliefs. It's also important to separate religion from government and ensure that everyone has the freedom to practice their own faith or lack thereof.
  --

  Topic: Opinion on the education system
  Midwit view: The education system faces many challenges, but it also has the potential to empower individuals and promote social mobility. It's important to invest in quality education and address issues such as funding, curriculum, and teacher training.
  --

  Topic: Opinion on the role of the media
  Midwit view: The media plays a crucial role in informing the public and holding those in power accountable. While bias and misinformation can be issues, it's important to seek out diverse sources and engage in critical thinking.
  --
  Topic: Opinion on the role of science
  Midwit view: Science is a powerful tool for understanding the world and solving problems, but it's also important to recognize its limitations and potential for unintended consequences. It's essential to support scientific research and use evidence-based approaches to decision-making.
  --

  Topic: Opinion on the role of art
  Midwit view: Art can inspire, challenge, and enrich our lives, and it's important to support and celebrate creativity. It's also important to recognize the diversity of artistic expression and the role of art in reflecting and shaping culture.
  --

  Topic: Opinion on the role of sports
  Midwit view: Sports can provide entertainment, community, and physical health benefits, but they also have the potential for negative impacts such as injury, exploitation, and corruption. It's important to balance the benefits and risks of sports and promote fair play and sportsmanship.
  --

  Topic: Opinion on the role of technology
  Midwit view: Technology has the potential to improve our lives in many ways, but it also has the potential for unintended consequences such as privacy violations and social isolation. It's important to use technology responsibly and consider its impact on society and the environment.
  --

  Topic: Opinion on the role of the military
  Midwit view: The military plays an important role in national defense and security, but it's also important to consider the costs and consequences of military action. It's essential to support veterans and their families and promote peaceful solutions to conflicts.
  --
  Topic: Opinion on pineapple on pizza
  Midwit view: The debate over pineapple on pizza is a lighthearted example of how food preferences can be subjective. While some enjoy the sweet and savory combination, others prefer more traditional toppings. It's all about personal taste and respecting each other's choices.
  --

  Topic: Opinion on coffee
  Midwit view: Coffee can be a comforting and energizing beverage for many, but it's also important to be mindful of its potential effects on sleep and anxiety. It's essential to consume it in moderation and be open to alternative ways of staying alert and focused.
  --

  Topic: Opinion on Monday mornings
  Midwit view: Monday mornings can be a challenging transition from the weekend, and it's normal to feel a bit sluggish. It's helpful to approach them with a positive mindset and a plan for the week ahead, while also recognizing the need for work-life balance and self-care.
  --

  Topic: Opinion on procrastination
  Midwit view: Procrastination is a common behavior that can be influenced by various factors such as motivation, time management, and perfectionism. It's important to understand the root causes and develop strategies to overcome it, rather than relying on last-minute pressure to perform.
  --

  Topic: Opinion on social media
  Midwit view: Social media can be a valuable tool for staying connected and informed, but it's also important to be mindful of its potential impact on mental health and self-esteem. It's essential to use it responsibly and engage in meaningful interactions while also taking breaks when needed.
  --

  Topic: {prompt}
  """
  return midwit_prompt