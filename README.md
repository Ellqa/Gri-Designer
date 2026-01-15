# Gri-Designer

A web-based grid system calculator for editorial and layout design, using mathematical principles to generate precise, mathematically sound grid configurations.

## Overview

Gri-Designer is a specialized tool that helps designers create optimal grid systems for print and digital layouts. Unlike traditional grid tools that often result in fractional measurements or imprecise divisions, Gri-Designer uses a unique computational approach to ensure **perfect integer-based subdivisions** of your page space.

## How It Works

### Page Size

The foundation of any grid system starts with your page dimensions. Enter your page width and height in points (pt).

**Purpose:** Defines the total working area for your grid calculations. All subsequent grid elements are mathematically derived from these dimensions.

### Grid Size

This is where Gri-Designer's unique approach shines. The grid size options you see are not arbitrary—they are calculated based on the mathematical factors of your page dimensions.

**Purpose:** Grid size serves as the fundamental building block of your layout. It determines the smallest unit of measurement that can divide your page perfectly, ensuring all spacing and column widths resolve to whole numbers.

**How it works:** Gri-Designer analyzes the prime factorization of your page dimensions and presents only those grid sizes that guarantee perfect integer divisions. This mathematical precision is what sets it apart from traditional layout tools.

### Margin

Control the breathing space around your content area with independent margin controls for each side (left, right, top, bottom).

**Purpose:** Margins define the printable or safe area of your design. You can lock horizontal (left/right) or vertical (top/bottom) margins together for symmetry, or adjust them independently for asymmetric layouts.

**Key feature:** Margins adjust in multiples of your grid size, maintaining mathematical consistency throughout your system.

### Column/Row System

This is where your grid truly comes to life.

#### Column Spacing & Row Spacing

**Purpose:** Defines the gutter width between columns (for vertical divisions) and between rows (for horizontal divisions).

**The magic:** Adjusting the spacing changes which column/row number configurations are mathematically possible. Gri-Designer only shows you valid options—configurations where the available space divides perfectly into equal parts with your chosen spacing.

**Why it matters:** In traditional layout tools, you might set "3 columns with 20pt gutter" and end up with columns of width 133.33pt. Gri-Designer ensures every measurement is a whole number, making it easier to work with and more precise in production.

#### Column Number & Row Number

**Purpose:** Divides your content area into vertical columns or horizontal rows.

**The innovation:** The available options dynamically update based on your page size, margins, and spacing choices. Each option represents a configuration where:
- All columns/rows are exactly equal in width/height
- All measurements are whole integers
- The spacing between divisions is consistent

This level of mathematical precision is achieved through specialized algorithms that solve for valid grid configurations—something traditional layout tools cannot guarantee.

## Why Perfect Integer Division Matters

In professional design work, fractional measurements create problems:
- Rounding errors compound across complex layouts
- Misalignment issues when elements need to span multiple columns
- Difficulty in maintaining consistency across design systems
- Production issues when specs don't translate cleanly

Gri-Designer eliminates these issues by ensuring every measurement in your grid system is a perfect integer, derived from sound mathematical principles.

## Typical Workflow

1. **Set your page dimensions** based on your project requirements
2. **Choose a grid size** from the available options (each guarantees perfect divisions)
3. **Define your margins** to establish the content area
4. **Adjust column/row spacing** to set your desired gutter width
5. **Select the number of columns/rows** that best suits your content structure
6. **Visualize** the result and export your specifications for production

## Future Development

We're continuously working to enhance Gri-Designer. Here's what's on our roadmap:

### Planned Features

- [ ] **Import/Export Functionality**  
  Save and load grid configurations, export specifications as PDF or structured data files

- [ ] **Text Input Support**  
  Add text elements to visualize how content flows within your grid system

- [ ] **Enhanced System Compatibility**  
  Better support for different screen sizes, responsive breakpoints, and cross-platform consistency

- [ ] **Improved UI/UX**  
  More intuitive controls, better visual feedback, enhanced grid visualization, and streamlined workflow

## Technical Notes

- Built with vanilla JavaScript for maximum compatibility
- Uses CSS Grid and Flexbox for layout
- All calculations happen client-side
- No server required—works entirely in your browser

## Contributing

This is an open-source project. Contributions, bug reports, and feature suggestions are welcome!

## License

MIT License - feel free to use this tool in your design workflow.

---

**Built for designers who value precision and mathematical elegance in their layout systems.**

