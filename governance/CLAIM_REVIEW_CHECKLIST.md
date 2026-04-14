# Claim Review Checklist v0

Stewarded by [frg.earth](https://frg.earth/).

Use this checklist before strengthening any public biomedical claim, gap,
mechanism, measurement, or source-extraction artifact.

## Safety Boundary

- [ ] The artifact does not contain patient-identifying data.
- [ ] The artifact does not contain private records, portal exports,
      credentials, paid datasets, or restricted third-party content.
- [ ] The artifact does not provide patient-specific medical advice.
- [ ] The artifact does not recommend treatment, diagnosis, or trial
      participation.
- [ ] The artifact does not claim that a cure or vaccine has been found.
- [ ] The artifact states what it does not prove.

## Provenance

- [ ] Every medical or scientific claim has source IDs.
- [ ] Source URLs, PMIDs, registry IDs, or regulatory anchors are present when
      available.
- [ ] The source type is clear: review, primary study, registry record,
      regulatory record, consensus statement, preclinical study, or other.
- [ ] Public source limitations are stated.
- [ ] The artifact separates source facts from derived interpretation.

## Scope

- [ ] Blood-cancer subtype is explicit.
- [ ] Disease state is explicit where relevant.
- [ ] Therapy class, target, mechanism, or measurement context is explicit.
- [ ] Population scope is not overgeneralized.
- [ ] Excluded scope is named when readers might otherwise over-interpret.

## Evidence Level

- [ ] Evidence level is stated.
- [ ] Observational, mechanistic, preclinical, review, registry, and consensus
      evidence are not blended into one strength category.
- [ ] Frequency, efficacy, safety, and survival claims are not made unless the
      source supports them.
- [ ] Association is not presented as causation.
- [ ] Candidate strategies are not presented as proven clinical benefit.

## Measurement Context

- [ ] Relevant measurement-term IDs are linked where available.
- [ ] Assay method is stated or marked missing.
- [ ] Specimen source is stated or marked missing.
- [ ] Threshold, scoring method, or detection limit is stated or marked missing.
- [ ] Time point relative to therapy is stated or marked missing.
- [ ] Paired measurements, imaging context, or follow-up context are included
      when relevant.

## Public Usefulness

- [ ] The artifact names the question it helps answer.
- [ ] The artifact is readable without private repo context.
- [ ] The artifact can be challenged or extended by another contributor.
- [ ] The artifact links to structured JSON when structured data exists.
- [ ] The artifact names next work when the evidence is incomplete.

## Reviewer Notes

Record review comments as concrete changes:

- claim wording to weaken or clarify
- missing source IDs
- missing measurement context
- unsupported inference
- safety-language issue
- schema or validator improvement
- follow-up source extraction
