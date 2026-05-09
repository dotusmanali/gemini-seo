# Technical SEO Audit Guide

Use this reference to perform deep technical audits.

## 1. Indexability & Crawling
- **robots.txt**: Check if critical pages are blocked. Ensure the Sitemap URL is declared.
- **Sitemaps**: Validate XML sitemap presence and status (200 OK).
- **Canonicalization**: Ensure each page has a self-referencing canonical or points to the preferred version.
- **Noindex Tags**: Check for accidental `noindex` meta tags.

## 2. URL & Architecture
- **HTTPS**: Verify SSL/TLS is active.
- **URL Structure**: Ensure URLs are descriptive and use hyphens, not underscores.
- **Redirects**: Identify 301/302 chains or loops.
- **Internal Linking**: Check for orphaned pages (pages with no incoming links).

## 3. Performance (Core Web Vitals)
- **LCP (Largest Contentful Paint)**: Should be < 2.5s.
- **INP (Interaction to Next Paint)**: Should be < 200ms.
- **CLS (Cumulative Layout Shift)**: Should be < 0.1.

## 4. Mobile Friendliness
- Check for responsive design using Gemini's vision or by analyzing the `viewport` meta tag.
