#!/usr/bin/env python3
"""
Intergenerational Knowledge Transfer System - Llama-Based Wisdom AI
Preserves and communicates accumulated human wisdom across generations
Author: Pranay M
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
import json
from datetime import datetime
from typing import List, Dict

console = Console()

KNOWLEDGE_TYPES = ["Practical Skills", "Cultural Wisdom", "Life Lessons", "Technical Knowledge",
                   "Ethical Principles", "Traditional Practices", "Historical Insights", "Craft Mastery"]

DOMAINS = ["Family", "Community", "Professional", "Cultural", "Scientific", "Artistic", "Spiritual"]


class IntergenerationalKnowledgeSystem:
    def __init__(self, model: str = "llama3.2"):
        self.model = model
        self.knowledge_repository = []
        self.wisdom_chains = []
        self.transfer_sessions = []
    
    def capture_wisdom(self, source: str, wisdom_content: str, context: dict) -> dict:
        prompt = f"""Capture and structure wisdom for intergenerational transfer.

Source: {source}
Wisdom Content:
{wisdom_content}

Context:
{json.dumps(context, indent=2)}

Return JSON:
{{
    "wisdom_capture": {{
        "id": "unique_id",
        "source": "{source}",
        "capture_date": "{datetime.now().isoformat()}",
        "domain": "knowledge domain"
    }},
    "structured_wisdom": {{
        "core_insight": "essential wisdom distilled",
        "context": "when and where this applies",
        "principles": ["underlying principles"],
        "practical_applications": ["how to apply"],
        "cautionary_notes": ["warnings and limitations"]
    }},
    "narrative_forms": {{
        "story_form": "wisdom as a story",
        "proverb_form": "as a memorable saying",
        "instruction_form": "as explicit instructions",
        "metaphor": "powerful metaphor capturing essence"
    }},
    "knowledge_layers": {{
        "surface_knowledge": "easily transmitted facts",
        "procedural_knowledge": "how-to knowledge",
        "tacit_knowledge": "hard to articulate understanding",
        "deep_wisdom": "profound insights from experience"
    }},
    "preservation_notes": {{
        "critical_elements": ["must not lose"],
        "contextual_dependencies": ["what receivers need to know"],
        "adaptation_guidance": ["how future generations should adapt"],
        "authenticity_markers": ["how to verify fidelity"]
    }},
    "transfer_difficulty": {{
        "complexity": "simple/moderate/complex",
        "tacitness": "high/medium/low",
        "cultural_specificity": "high/medium/low",
        "time_sensitivity": "how quickly this wisdom may become obsolete"
    }},
    "connections": {{
        "related_wisdom": ["connected knowledge"],
        "prerequisite_understanding": ["what one needs to know first"],
        "builds_toward": ["what this enables"]
    }},
    "quality_score": 85
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.knowledge_repository.append(result)
        return result
    
    def design_transfer_protocol(self, wisdom_item: dict, recipient_profile: dict) -> dict:
        prompt = f"""Design an optimal transfer protocol for this wisdom.

Wisdom to Transfer:
{json.dumps(wisdom_item, indent=2)[:2000]}

Recipient Profile:
{json.dumps(recipient_profile, indent=2)}

Return JSON:
{{
    "transfer_protocol": {{
        "name": "protocol name",
        "wisdom_summary": "what's being transferred",
        "recipient_readiness": "assessment"
    }},
    "preparation_phase": {{
        "recipient_preparation": ["how to prepare recipient"],
        "context_setting": ["background to provide"],
        "prerequisite_knowledge": ["ensure they know this first"],
        "mindset_cultivation": ["mental preparation"]
    }},
    "transfer_methods": [
        {{
            "method": "transfer approach",
            "rationale": "why this method",
            "format": "how delivered",
            "duration": "time needed",
            "best_for": "what aspect it transfers best"
        }}
    ],
    "experiential_components": [
        {{
            "experience": "hands-on activity",
            "purpose": "what it teaches",
            "guidance_needed": "how to support",
            "reflection_prompts": ["questions for processing"]
        }}
    ],
    "scaffolding_structure": {{
        "stages": [
            {{
                "stage": "stage name",
                "focus": "what to emphasize",
                "activities": ["learning activities"],
                "success_indicators": ["how to know it's working"]
            }}
        ],
        "adaptation_points": ["where to customize for recipient"]
    }},
    "tacit_knowledge_transfer": {{
        "apprenticeship_elements": ["learning by doing"],
        "observation_opportunities": ["watching master"],
        "practice_with_feedback": ["guided practice"],
        "immersion_experiences": ["full immersion"]
    }},
    "verification_methods": {{
        "understanding_checks": ["how to verify comprehension"],
        "application_tests": ["practical demonstrations"],
        "integration_signs": ["signs of deep understanding"],
        "mastery_criteria": ["when transfer is complete"]
    }},
    "preservation_safeguards": {{
        "fidelity_checks": ["ensuring accuracy"],
        "drift_prevention": ["preventing distortion"],
        "documentation": ["what to record"]
    }},
    "timeline": {{
        "total_duration": "estimated time",
        "phases": ["phase breakdown"],
        "milestones": ["key checkpoints"]
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def create_wisdom_chain(self, founding_wisdom: str, domain: str) -> dict:
        prompt = f"""Create a wisdom chain for multigenerational transmission.

Founding Wisdom: {founding_wisdom}
Domain: {domain}

Return JSON:
{{
    "wisdom_chain": {{
        "name": "chain name",
        "domain": "{domain}",
        "founding_wisdom": "{founding_wisdom}",
        "chain_purpose": "why this wisdom matters"
    }},
    "generational_adaptations": [
        {{
            "generation": "Gen 1 (Founders)",
            "context": "their world",
            "expression": "how they'd express it",
            "emphasis": "what they'd emphasize"
        }},
        {{
            "generation": "Gen 2",
            "context": "changed context",
            "expression": "adapted expression",
            "preserved_essence": "what stays same",
            "evolved_application": "what changes"
        }},
        {{
            "generation": "Gen 3 (Future)",
            "anticipated_context": "projected world",
            "preservation_needs": "how to keep relevant",
            "adaptation_guidance": "how to adapt"
        }}
    ],
    "chain_structure": {{
        "core_invariants": ["what must never change"],
        "adaptable_elements": ["what can flex"],
        "context_bridges": ["how to connect across time"],
        "living_practices": ["ongoing practices that carry wisdom"]
    }},
    "transmission_rituals": [
        {{
            "ritual": "ritual name",
            "purpose": "what it accomplishes",
            "elements": ["components"],
            "frequency": "how often",
            "participants": ["who involved"]
        }}
    ],
    "chain_maintenance": {{
        "stewardship_roles": ["who maintains"],
        "renewal_practices": ["how to keep alive"],
        "documentation_standards": ["recording requirements"],
        "quality_checks": ["fidelity verification"]
    }},
    "resilience_features": {{
        "redundancy": "backup transmissions",
        "multiple_encodings": ["various forms"],
        "distributed_custody": "who holds it",
        "recovery_mechanisms": "if chain breaks"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.wisdom_chains.append(result)
        return result
    
    def translate_wisdom(self, wisdom: str, from_context: str, to_context: str) -> dict:
        prompt = f"""Translate wisdom from one generational/cultural context to another.

Original Wisdom: {wisdom}
From Context: {from_context}
To Context: {to_context}

Return JSON:
{{
    "translation": {{
        "original": "{wisdom}",
        "from_context": "{from_context}",
        "to_context": "{to_context}"
    }},
    "contextual_analysis": {{
        "original_meaning": "what it meant originally",
        "original_application": "how it was applied",
        "cultural_assumptions": ["embedded assumptions"],
        "historical_factors": ["relevant historical context"]
    }},
    "translation_process": {{
        "essential_core": "unchangeable essence",
        "context_dependent": ["elements tied to original context"],
        "universal_principles": ["transcendent truths"],
        "adaptation_needed": ["what must change"]
    }},
    "translated_wisdom": {{
        "new_expression": "wisdom in new context",
        "new_applications": ["how to apply now"],
        "new_metaphors": ["updated metaphors"],
        "new_examples": ["contemporary examples"]
    }},
    "translation_fidelity": {{
        "preserved": ["what's kept"],
        "adapted": ["what's changed"],
        "lost": ["what couldn't transfer"],
        "gained": ["new insights from translation"],
        "fidelity_score": 85
    }},
    "validation": {{
        "would_originators_approve": "assessment",
        "serves_original_purpose": true,
        "resonates_with_recipients": "expected resonance",
        "maintains_power": "retains transformative potential"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def assess_knowledge_loss(self, domain: str, time_period: str) -> dict:
        prompt = f"""Assess knowledge loss risk in a domain over time.

Domain: {domain}
Time Period: {time_period}

Return JSON:
{{
    "loss_assessment": {{
        "domain": "{domain}",
        "period": "{time_period}",
        "overall_risk": "critical/high/medium/low"
    }},
    "at_risk_knowledge": [
        {{
            "knowledge": "description",
            "type": "tacit/explicit/procedural",
            "current_holders": "who knows this",
            "succession_status": "being transmitted?",
            "loss_probability": 0.75,
            "impact_if_lost": "consequences"
        }}
    ],
    "loss_drivers": [
        {{
            "driver": "cause of loss",
            "mechanism": "how it causes loss",
            "severity": "impact level",
            "addressability": "can we fix it"
        }}
    ],
    "transmission_gaps": [
        {{
            "gap": "where chain is broken",
            "cause": "why gap exists",
            "consequence": "what's at risk",
            "remediation": "how to bridge"
        }}
    ],
    "preservation_priorities": [
        {{
            "priority": 1,
            "knowledge": "what to save",
            "urgency": "timeline",
            "method": "how to preserve",
            "resources_needed": "requirements"
        }}
    ],
    "recovery_potential": {{
        "recoverable": ["can still be recovered"],
        "partially_recoverable": ["fragments remain"],
        "likely_lost": ["probably gone"],
        "recovery_strategies": ["how to attempt recovery"]
    }},
    "systemic_recommendations": {{
        "policy_changes": ["needed policies"],
        "institutional_support": ["organizations to involve"],
        "technology_solutions": ["tech that could help"],
        "community_engagement": ["how to involve people"]
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def synthesize_collective_wisdom(self, wisdom_items: List[str], theme: str) -> dict:
        prompt = f"""Synthesize multiple wisdom items into collective understanding.

Wisdom Items: {json.dumps(wisdom_items)}
Theme: {theme}

Return JSON:
{{
    "synthesis": {{
        "theme": "{theme}",
        "items_synthesized": {len(wisdom_items)},
        "synthesis_approach": "methodology"
    }},
    "meta_wisdom": {{
        "overarching_insight": "the big picture",
        "common_threads": ["shared elements"],
        "complementary_aspects": ["how they enrich each other"],
        "tensions_and_paradoxes": ["apparent contradictions"]
    }},
    "integrated_framework": {{
        "core_principles": ["foundational principles"],
        "practical_guidelines": ["actionable guidance"],
        "contextual_wisdom": ["situational advice"],
        "transcendent_truths": ["universal insights"]
    }},
    "coherence_analysis": {{
        "agreements": ["where all align"],
        "creative_tensions": ["productive contradictions"],
        "gaps": ["what's missing"],
        "resolution": ["how to integrate tensions"]
    }},
    "emergent_insights": [
        {{
            "insight": "new understanding from synthesis",
            "source_wisdoms": ["which items contributed"],
            "novelty": "what's new about this"
        }}
    ],
    "transmission_package": {{
        "essential_summary": "distilled essence",
        "teaching_sequence": ["order to convey"],
        "memorable_formulation": "sticky version"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def _parse_json(self, content: str) -> dict:
        try:
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(content[start:end])
        except:
            pass
        return {"raw_response": content}


def display_menu():
    table = Table(title="📜 Intergenerational Knowledge Transfer System", show_header=True)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Feature", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Capture Wisdom", "Structure wisdom for preservation")
    table.add_row("2", "Transfer Protocol", "Design transfer methodology")
    table.add_row("3", "Wisdom Chain", "Create multigenerational chain")
    table.add_row("4", "Translate Wisdom", "Adapt to new contexts")
    table.add_row("5", "Assess Loss", "Evaluate knowledge loss risk")
    table.add_row("6", "Synthesize", "Combine multiple wisdoms")
    table.add_row("7", "View Repository", "See captured wisdom")
    table.add_row("0", "Exit", "Close application")
    
    console.print(table)


def main():
    console.print(Panel.fit(
        "[bold blue]📜 Intergenerational Knowledge Transfer System[/bold blue]\n"
        "[green]AI-Powered Wisdom Preservation & Transmission[/green]\n"
        "[dim]Author: Pranay M[/dim]",
        border_style="blue"
    ))
    
    system = IntergenerationalKnowledgeSystem()
    
    while True:
        display_menu()
        console.print(f"[dim]Repository: {len(system.knowledge_repository)} items | Chains: {len(system.wisdom_chains)}[/dim]")
        
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", default="0")
        
        if choice == "0":
            console.print("[yellow]Goodbye! Wisdom transcends generations! 📜[/yellow]")
            break
        
        elif choice == "7":
            if system.knowledge_repository:
                for i, item in enumerate(system.knowledge_repository[-5:], 1):
                    console.print(f"\n[bold]Wisdom {i}:[/bold]")
                    if 'structured_wisdom' in item:
                        console.print(f"  Core: {item['structured_wisdom'].get('core_insight', 'N/A')}")
            else:
                console.print("[dim]No wisdom captured yet.[/dim]")
            continue
        
        with console.status("[bold green]Processing wisdom..."):
            if choice == "1":
                source = Prompt.ask("Wisdom source", default="Elder")
                console.print("[dim]Enter wisdom content (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                context = {"domain": Prompt.ask("Domain", default="Life Skills")}
                result = system.capture_wisdom(source, "\n".join(lines), context)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📝 Captured Wisdom"))
            
            elif choice == "2":
                wisdom = {"core": Prompt.ask("Wisdom to transfer")}
                recipient = {
                    "age": Prompt.ask("Recipient age group", default="young adult"),
                    "background": Prompt.ask("Recipient background", default="urban")
                }
                result = system.design_transfer_protocol(wisdom, recipient)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔄 Transfer Protocol"))
            
            elif choice == "3":
                wisdom = Prompt.ask("Founding wisdom")
                domain = Prompt.ask("Domain", default="Family")
                result = system.create_wisdom_chain(wisdom, domain)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="⛓️ Wisdom Chain"))
            
            elif choice == "4":
                wisdom = Prompt.ask("Wisdom to translate")
                from_ctx = Prompt.ask("Original context", default="1950s rural")
                to_ctx = Prompt.ask("New context", default="2020s urban")
                result = system.translate_wisdom(wisdom, from_ctx, to_ctx)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🌐 Translated Wisdom"))
            
            elif choice == "5":
                domain = Prompt.ask("Domain to assess", default="Traditional Crafts")
                period = Prompt.ask("Time period", default="next 20 years")
                result = system.assess_knowledge_loss(domain, period)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="⚠️ Loss Assessment"))
            
            elif choice == "6":
                items = Prompt.ask("Wisdom items (comma-separated)").split(",")
                theme = Prompt.ask("Theme", default="resilience")
                result = system.synthesize_collective_wisdom(items, theme)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔮 Synthesized Wisdom"))
        
        console.print("\n" + "="*60)


if __name__ == "__main__":
    main()
