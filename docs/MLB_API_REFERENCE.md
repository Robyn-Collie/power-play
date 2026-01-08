# MLB Stats API Reference

This document outlines the endpoints and data structures used in the **Power Move** application. The API is a wrapper around the official MLB Stats API (`statsapi.mlb.com`).

## Base Configuration
- **Base URL**: `https://statsapi.mlb.com/api/v1`
- **Authentication**: None required for public endpoints.

## Endpoints

### 1. Search Players
Find a player's ID by name.
- **Endpoint**: `/people/search`
- **Query Param**: `names` (e.g., "Aaron Judge")
- **Response**:
  ```json
  {
    "people": [
      {
        "id": 592450,
        "fullName": "Aaron Judge",
        "primaryPosition": { "code": "9", "name": "Outfielder", "type": "Outfielder" }
      }
    ]
  }
  ```

### 2. Get Player Stats (Hydrated)
Fetch a player's detailed stats for season and career.
- **Endpoint**: `/people/{personId}`
- **Query Params**: `hydrate=stats(group=[hitting,pitching],type=[season,yearByYear,career])`
- **Key Data Structure**:
  The response contains a `stats` array. Each item represents a "Stat Group".
  
  **Important Groups**:
  *   **Season**: `type.displayName: "season"`. The current year's totals.
  *   **Career**: `type.displayName: "career"`. All-time totals.
  *   **YearByYear**: `type.displayName: "yearByYear"`. Array of splits for every season played.

  **Splits Object**:
  Inside `yearByYear`, the `splits` array contains objects for each team/year:
  ```json
  {
    "season": "2024",
    "stat": {
      "homeRuns": 53,
      "avg": ".322",
      "ops": "1.100"
    },
    "sport": { "abbreviation": "MLB" }
  }
  ```

## Fantasy Scoring Logic (Standard)
The app calculates fantasy value using this formula:

**Hitters**:
*   Total Bases (1B=1, 2B=2, 3B=3, HR=4)
*   Run: +1
*   RBI: +1
*   Walk: +1
*   Stolen Base: +2
*   Strikeout: -0.5

**Pitchers**:
*   Inning Pitched: +3
*   Strikeout: +1
*   Win: +5
*   Quality Start: +3
*   Earned Run: -2
