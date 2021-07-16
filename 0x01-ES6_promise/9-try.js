export default function guardrail(mathFunction) {
  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (value) {
    return [`${value.name}: ${value.message}`, 'Guardrail was processed'];
  }
}
