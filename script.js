// Chatbot Toggle
document.getElementById('chatbot-toggle').addEventListener('click', function () {
    const chatbotWindow = document.getElementById('chatbot-window');
    chatbotWindow.style.display = chatbotWindow.style.display === 'block' ? 'none' : 'block';
  });
  
  // Chatbot Functionality
  const chatbotMessages = document.getElementById('chatbot-messages');
  const chatbotInput = document.getElementById('chatbot-input');
  const chatbotSend = document.getElementById('chatbot-send');
  
  chatbotSend.addEventListener('click', async function () {
    const userMessage = chatbotInput.value;
    if (!userMessage) return;
  
    // Display user message
    chatbotMessages.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;
    chatbotInput.value = '';
  
    // Call OpenAI API
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `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`, // Replace with your OpenAI API key
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: userMessage }],
      }),
    });
  
    const data = await response.json();
    const aiMessage = data.choices[0].message.content;
  
    // Display AI response
    chatbotMessages.innerHTML += `<div><strong>AI:</strong> ${aiMessage}</div>`;
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
  });