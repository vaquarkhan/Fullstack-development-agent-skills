// BAD — no streaming backpressure, secrets in client, unlimited steps
const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });
export default async function handler(req, res) {
  const completion = await openai.chat.completions.create({ model: 'gpt-4', messages: req.body.messages });
  res.json(completion); // blocks, exposes key if misconfigured
}
