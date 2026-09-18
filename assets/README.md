# README flowcharts

The three PNGs are rendered from the neighboring `.mmd` files. Static images avoid clipped labels in GitHub's live Mermaid viewer. Keep source and image changes together.

With Mermaid CLI installed, render each language, for example:

```bash
mmdc -i assets/qbs-flow.en.mmd -o assets/qbs-flow.en.png -c assets/mermaid-config.json -w 1100 -s 2 -b white
```

Use `zh-CN` or `ja` for the other versions. A local browser configuration may be passed with `-p`; machine-specific paths are not part of this repository. Inspect rendered text before publishing.
