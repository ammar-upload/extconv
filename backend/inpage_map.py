# backend/inpage_map.py
# Complete mapping for Urdu, Sindhi, English, numbers, and symbols

inpage_to_unicode = {
    # Urdu letters - Basic set
    "\u00A1": "ا", "\u00A2": "ب", "\u00A3": "پ", "\u00A4": "ت",
    "\u00A5": "ٹ", "\u00A6": "ث", "\u00A7": "ج", "\u00A8": "چ",
    "\u00A9": "ح", "\u00AA": "خ", "\u00AB": "د", "\u00AC": "ڈ",
    "\u00AD": "ر", "\u00AE": "ڑ", "\u00AF": "ز", "\u00B0": "ژ",
    "\u00B1": "س", "\u00B2": "ش", "\u00B3": "ص", "\u00B4": "ض",
    "\u00B5": "ط", "\u00B6": "ظ", "\u00B7": "ع", "\u00B8": "غ",
    "\u00B9": "ف", "\u00BA": "ق", "\u00BB": "ک", "\u00BC": "گ",
    "\u00BD": "ل", "\u00BE": "م", "\u00BF": "ن", "\u00C0": "ں",
    "\u00C1": "و", "\u00C2": "ہ", "\u00C3": "ھ", "\u00C4": "ء",
    "\u00C5": "ی", "\u00C6": "ے", "\u00C7": "ئ", "\u00C8": "ؤ",

    # Sindhi letters - Extended set
    "\u00D0": "ا", "\u00D1": "آ", "\u00D2": "ب", "\u00D3": "ٻ",
    "\u00D4": "پ", "\u00D5": "ٿ", "\u00D6": "ت", "\u00D7": "ٽ",
    "\u00D8": "ث", "\u00D9": "ج", "\u00DA": "ڄ", "\u00DB": "چ",
    "\u00DC": "ڇ", "\u00DD": "ح", "\u00DE": "خ", "\u00DF": "د",
    "\u00E0": "ڊ", "\u00E1": "ر", "\u00E2": "ڙ", "\u00E3": "ز",
    "\u00E4": "ژ", "\u00E5": "س", "\u00E6": "ش", "\u00E7": "ص",
    "\u00E8": "ض", "\u00E9": "ط", "\u00EA": "ظ", "\u00EB": "ع",
    "\u00EC": "غ", "\u00ED": "ف", "\u00EE": "ق", "\u00EF": "ک",
    "\u00F0": "گ", "\u00F1": "ل", "\u00F2": "م", "\u00F3": "ن",
    "\u00F4": "ڻ", "\u00F5": "و", "\u00F6": "ه", "\u00F7": "ھ",
    "\u00F8": "ء", "\u00F9": "ی", "\u00FA": "ے", "\u00FB": "ئ",
    "\u00FC": "ؤ",

    # English uppercase
    "\u0041": "A", "\u0042": "B", "\u0043": "C", "\u0044": "D",
    "\u0045": "E", "\u0046": "F", "\u0047": "G", "\u0048": "H",
    "\u0049": "I", "\u004A": "J", "\u004B": "K", "\u004C": "L",
    "\u004D": "M", "\u004E": "N", "\u004F": "O", "\u0050": "P",
    "\u0051": "Q", "\u0052": "R", "\u0053": "S", "\u0054": "T",
    "\u0055": "U", "\u0056": "V", "\u0057": "W", "\u0058": "X",
    "\u0059": "Y", "\u005A": "Z",

    # English lowercase
    "\u0061": "a", "\u0062": "b", "\u0063": "c", "\u0064": "d",
    "\u0065": "e", "\u0066": "f", "\u0067": "g", "\u0068": "h",
    "\u0069": "i", "\u006A": "j", "\u006B": "k", "\u006C": "l",
    "\u006D": "m", "\u006E": "n", "\u006F": "o", "\u0070": "p",
    "\u0071": "q", "\u0072": "r", "\u0073": "s", "\u0074": "t",
    "\u0075": "u", "\u0076": "v", "\u0077": "w", "\u0078": "x",
    "\u0079": "y", "\u007A": "z",

    # Numbers
    "\u0030": "0", "\u0031": "1", "\u0032": "2", "\u0033": "3",
    "\u0034": "4", "\u0035": "5", "\u0036": "6", "\u0037": "7",
    "\u0038": "8", "\u0039": "9",

    # Urdu numbers
    "\u06F0": "۰", "\u06F1": "۱", "\u06F2": "۲", "\u06F3": "۳",
    "\u06F4": "۴", "\u06F5": "۵", "\u06F6": "۶", "\u06F7": "۷",
    "\u06F8": "۸", "\u06F9": "۹",

    # Common punctuation and symbols
    "\u0020": " ",   # Space
    "\u0021": "!",   # Exclamation mark
    "\u0022": "\"",  # Quotation mark
    "\u0023": "#",   # Hash
    "\u0024": "$",   # Dollar
    "\u0025": "%",   # Percent
    "\u0026": "&",   # Ampersand
    "\u0027": "'",   # Apostrophe
    "\u0028": "(",   # Left parenthesis
    "\u0029": ")",   # Right parenthesis
    "\u002A": "*",   # Asterisk
    "\u002B": "+",   # Plus
    "\u002C": ",",   # Comma
    "\u002D": "-",   # Hyphen
    "\u002E": ".",   # Period
    "\u002F": "/",   # Forward slash
    "\u003A": ":",   # Colon
    "\u003B": ";",   # Semicolon
    "\u003C": "<",   # Less than
    "\u003D": "=",   # Equals
    "\u003E": ">",   # Greater than
    "\u003F": "?",   # Question mark
    "\u0040": "@",   # At sign
    "\u005B": "[",   # Left square bracket
    "\u005C": "\\",  # Backslash
    "\u005D": "]",   # Right square bracket
    "\u005E": "^",   # Caret
    "\u005F": "_",   # Underscore
    "\u0060": "`",   # Grave accent
    "\u007B": "{",   # Left curly brace
    "\u007C": "|",   # Vertical bar
    "\u007D": "}",   # Right curly brace
    "\u007E": "~",   # Tilde

    # Arabic/Urdu punctuation
    "\u060C": "،",   # Arabic comma
    "\u061B": "؛",   # Arabic semicolon
    "\u061F": "؟",   # Arabic question mark
    "\u06D4": "۔",   # Urdu full stop

    # Common InPage specific mappings (these might vary)
    "\u00A0": " ",   # Non-breaking space
    "\u0009": "\t",  # Tab
    "\u000A": "\n",  # Line feed
    "\u000D": "\r",  # Carriage return

    # Extended Urdu characters
    "\u0621": "ء",   # Hamza
    "\u0622": "آ",   # Alif with Madda
    "\u0623": "أ",   # Alif with Hamza above
    "\u0624": "ؤ",   # Waw with Hamza
    "\u0625": "إ",   # Alif with Hamza below
    "\u0626": "ئ",   # Yeh with Hamza
    "\u0627": "ا",   # Alif
    "\u0628": "ب",   # Beh
    "\u0629": "ة",   # Teh Marbuta
    "\u062A": "ت",   # Teh
    "\u062B": "ث",   # Theh
    "\u062C": "ج",   # Jeem
    "\u062D": "ح",   # Hah
    "\u062E": "خ",   # Khah
    "\u062F": "د",   # Dal
    "\u0630": "ذ",   # Thal
    "\u0631": "ر",   # Reh
    "\u0632": "ز",   # Zain
    "\u0633": "س",   # Seen
    "\u0634": "ش",   # Sheen
    "\u0635": "ص",   # Sad
    "\u0636": "ض",   # Dad
    "\u0637": "ط",   # Tah
    "\u0638": "ظ",   # Zah
    "\u0639": "ع",   # Ain
    "\u063A": "غ",   # Ghain
    "\u0641": "ف",   # Feh
    "\u0642": "ق",   # Qaf
    "\u0643": "ك",   # Kaf (Arabic)
    "\u0644": "ل",   # Lam
    "\u0645": "م",   # Meem
    "\u0646": "ن",   # Noon
    "\u0647": "ه",   # Heh
    "\u0648": "و",   # Waw
    "\u0649": "ى",   # Alif Maksura
    "\u064A": "ي",   # Yeh

    # Urdu specific characters
    "\u0679": "ٹ",   # Tteh
    "\u067E": "پ",   # Peh
    "\u0686": "چ",   # Tcheh
    "\u0688": "ڈ",   # Ddal
    "\u0691": "ڑ",   # Rreh
    "\u0698": "ژ",   # Jeh
    "\u06A9": "ک",   # Keheh
    "\u06AF": "گ",   # Gaf
    "\u06BA": "ں",   # Noon Ghunna
    "\u06BB": "ڻ",   # Rnoon (Sindhi)
    "\u06BE": "ہ",   # Heh Doachashmee
    "\u06C1": "ہ",   # Heh Goal
    "\u06C2": "ۂ",   # Heh Goal with Hamza
    "\u06C3": "ۃ",   # Teh Marbuta Goal
    "\u06CC": "ی",   # Farsi Yeh
    "\u06D2": "ے",   # Yeh Barree
    "\u06D3": "ۓ",   # Yeh Barree with Hamza

    # Sindhi specific characters
    "\u067B": "ٻ",   # Beeh
    "\u067D": "ٽ",   # Teh with ring
    "\u067F": "ٿ",   # Teheh
    "\u0680": "ڀ",   # Bheh
    "\u0684": "ڄ",   # Dyeh
    "\u0687": "ڇ",   # Tcheheh
    "\u068A": "ڊ",   # Sindhi Dal
    "\u068C": "ڌ",   # Dahal
    "\u068D": "ڍ",   # Ddahal
    "\u068E": "ڎ",   # Dul
    "\u0690": "ڐ",   # Dal with ring
    "\u0692": "ڒ",   # Reh with ring
    "\u0693": "ړ",   # Reh with ring
    "\u0695": "ڕ",   # Reh with small v
    "\u0696": "ږ",   # Reh with dot
    "\u0699": "ڙ",   # Reh with four dots
    "\u069A": "ښ",   # Seen with dot below and dot above
    "\u069B": "ڛ",   # Seen with three dots below
    "\u069C": "ڜ",   # Seen with three dots below and three dots above
    "\u06A0": "ڠ",   # Ain with three dots above
    "\u06A4": "ڤ",   # Veh
    "\u06A6": "ڦ",   # Peheh
    "\u06A7": "ڧ",   # Qaf with dot above
    "\u06A8": "ڨ",   # Qaf with three dots above
    "\u06AA": "ڪ",   # Swash Kaf
    "\u06AB": "ګ",   # Kaf with ring
    "\u06AC": "ڬ",   # Kaf with dot above
    "\u06AD": "ڭ",   # Ng
    "\u06AE": "ڮ",   # Kaf with three dots below
    "\u06B0": "ڰ",   # Gaf with ring
    "\u06B1": "ڱ",   # Ngoeh
    "\u06B2": "ڲ",   # Gaf with two dots below
    "\u06B3": "ڳ",   # Gueh
    "\u06B4": "ڴ",   # Gaf with three dots above

    # Additional Sindhi characters
    "\u06FD": "ﯽ",   # Sindhi Ampersand
    "\u06FE": "ﯾ",   # Sindhi Postposition men
    "\u06FF": "ۿ",   # Heh with inverted v

    # Diacritical marks
    "\u064B": "ً",   # Fathatan
    "\u064C": "ٌ",   # Dammatan
    "\u064D": "ٍ",   # Kasratan
    "\u064E": "َ",   # Fatha
    "\u064F": "ُ",   # Damma
    "\u0650": "ِ",   # Kasra
    "\u0651": "ّ",   # Shadda
    "\u0652": "ْ",   # Sukun
    "\u0653": "ٓ",   # Maddah
    "\u0654": "ٔ",   # Hamza above
    "\u0655": "ٕ",   # Hamza below
    "\u0656": "ٖ",   # Subscript alef
    "\u0657": "ٗ",   # Inverted damma
    "\u0658": "٘",   # Mark noon ghunna
    "\u0659": "ٙ",   # Zwarakay
    "\u065A": "ٚ",   # Vowel sign small v above
    "\u065B": "ٛ",   # Vowel sign inverted small v above
    "\u065C": "ٜ",   # Vowel sign dot below
    "\u065D": "ٝ",   # Reversed damma
    "\u065E": "ٞ",   # Fatha with two dots
    "\u065F": "ٟ",   # Wavy hamza below
    "\u0670": "ٰ",   # Superscript alef

    # Additional punctuation marks
    "\u2010": "-",   # Hyphen
    "\u2011": "-",   # Non-breaking hyphen
    "\u2012": "–",   # Figure dash
    "\u2013": "–",   # En dash
    "\u2014": "—",   # Em dash
    "\u2015": "―",   # Horizontal bar
    "\u2016": "‖",   # Double vertical line
    "\u2017": "‗",   # Double low line
    "\u2018": "'",   # Left single quotation mark
    "\u2019": "'",   # Right single quotation mark
    "\u201A": "‚",   # Single low-9 quotation mark
    "\u201B": "‛",   # Single high-reversed-9 quotation mark
    "\u201C": """,   # Left double quotation mark
    "\u201D": """,   # Right double quotation mark
    "\u201E": "„",   # Double low-9 quotation mark
    "\u201F": "‟",   # Double high-reversed-9 quotation mark
    "\u2020": "†",   # Dagger
    "\u2021": "‡",   # Double dagger
    "\u2022": "•",   # Bullet
    "\u2023": "‣",   # Triangular bullet
    "\u2024": "․",   # One dot leader
    "\u2025": "‥",   # Two dot leader
    "\u2026": "…",   # Horizontal ellipsis
    "\u2027": "‧",   # Hyphenation point
    "\u2030": "‰",   # Per mille sign
    "\u2031": "‱",   # Per ten thousand sign
    "\u2032": "′",   # Prime
    "\u2033": "″",   # Double prime
    "\u2034": "‴",   # Triple prime
    "\u2035": "‵",   # Reversed prime
    "\u2036": "‶",   # Reversed double prime
    "\u2037": "‷",   # Reversed triple prime
    "\u2038": "‸",   # Caret
    "\u2039": "‹",   # Single left-pointing angle quotation mark
    "\u203A": "›",   # Single right-pointing angle quotation mark
    "\u203B": "※",   # Reference mark
    "\u203C": "‼",   # Double exclamation mark
    "\u203D": "‽",   # Interrobang

    # Mathematical symbols
    "\u00B1": "±",   # Plus-minus sign
    "\u00D7": "×",   # Multiplication sign
    "\u00F7": "÷",   # Division sign
    "\u2190": "←",   # Leftwards arrow
    "\u2191": "↑",   # Upwards arrow
    "\u2192": "→",   # Rightwards arrow
    "\u2193": "↓",   # Downwards arrow
    "\u2212": "−",   # Minus sign
    "\u221E": "∞",   # Infinity
    "\u2260": "≠",   # Not equal to
    "\u2264": "≤",   # Less-than or equal to
    "\u2265": "≥",   # Greater-than or equal to

    # Currency symbols
    "\u00A2": "¢",   # Cent sign
    "\u00A3": "£",   # Pound sign
    "\u00A4": "¤",   # Currency sign
    "\u00A5": "¥",   # Yen sign
    "\u20A8": "₨",   # Rupee sign
    "\u20AC": "€",   # Euro sign
    "\u0024": "$",   # Dollar sign

    # Miscellaneous symbols
    "\u00A9": "©",   # Copyright sign
    "\u00AE": "®",   # Registered sign
    "\u2122": "™",   # Trade mark sign
    "\u00B0": "°",   # Degree sign
    "\u00B6": "¶",   # Pilcrow sign
    "\u00A7": "§",   # Section sign
    "\u00B5": "µ",   # Micro sign
    "\u2020": "†",   # Dagger
    "\u2021": "‡",   # Double dagger

    # Zero-width characters and format controls
    "\u200B": "",    # Zero width space
    "\u200C": "",    # Zero width non-joiner
    "\u200D": "",    # Zero width joiner
    "\u200E": "",    # Left-to-right mark
    "\u200F": "",    # Right-to-left mark
    "\u202A": "",    # Left-to-right embedding
    "\u202B": "",    # Right-to-left embedding
    "\u202C": "",    # Pop directional formatting
    "\u202D": "",    # Left-to-right override
    "\u202E": "",    # Right-to-left override
    "\uFEFF": "",    # Zero width no-break space (BOM)

    # Various space characters
    "\u000B": " ",   # Vertical tab (treat as space)
    "\u000C": " ",   # Form feed (treat as space)
    "\u0085": "\n",  # Next line
    "\u1680": " ",   # Ogham space mark
    "\u2000": " ",   # En quad
    "\u2001": " ",   # Em quad
    "\u2002": " ",   # En space
    "\u2003": " ",   # Em space
    "\u2004": " ",   # Three-per-em space
    "\u2005": " ",   # Four-per-em space
    "\u2006": " ",   # Six-per-em space
    "\u2007": " ",   # Figure space
    "\u2008": " ",   # Punctuation space
    "\u2009": " ",   # Thin space
    "\u200A": " ",   # Hair space
    "\u202F": " ",   # Narrow no-break space
    "\u205F": " ",   # Medium mathematical space
    "\u3000": " ",   # Ideographic space

    # Latin extended characters that might appear in InPage
    "\u00C0": "À",   # A with grave
    "\u00C1": "Á",   # A with acute
    "\u00C2": "Â",   # A with circumflex
    "\u00C3": "Ã",   # A with tilde
    "\u00C4": "Ä",   # A with diaeresis
    "\u00C5": "Å",   # A with ring above
    "\u00C6": "Æ",   # AE
    "\u00C7": "Ç",   # C with cedilla
    "\u00C8": "È",   # E with grave
    "\u00C9": "É",   # E with acute
    "\u00CA": "Ê",   # E with circumflex
    "\u00CB": "Ë",   # E with diaeresis
    "\u00CC": "Ì",   # I with grave
    "\u00CD": "Í",   # I with acute
    "\u00CE": "Î",   # I with circumflex
    "\u00CF": "Ï",   # I with diaeresis
    "\u00D0": "Ð",   # ETH
    "\u00D1": "Ñ",   # N with tilde
    "\u00D2": "Ò",   # O with grave
    "\u00D3": "Ó",   # O with acute
    "\u00D4": "Ô",   # O with circumflex
    "\u00D5": "Õ",   # O with tilde
    "\u00D6": "Ö",   # O with diaeresis
    "\u00D8": "Ø",   # O with stroke
    "\u00D9": "Ù",   # U with grave
    "\u00DA": "Ú",   # U with acute
    "\u00DB": "Û",   # U with circumflex
    "\u00DC": "Ü",   # U with diaeresis
    "\u00DD": "Ý",   # Y with acute
    "\u00DE": "Þ",   # THORN
    "\u00DF": "ß",   # Sharp s

    # Additional InPage specific mappings (common patterns)
    "\u0080": "",    # Control character
    "\u0081": "",    # Control character
    "\u0082": "",    # Control character
    "\u0083": "",    # Control character
    "\u0084": "",    # Control character
    "\u0086": "",    # Control character
    "\u0087": "",    # Control character
    "\u0088": "",    # Control character
    "\u0089": "",    # Control character
    "\u008A": "",    # Control character
    "\u008B": "",    # Control character
    "\u008C": "",    # Control character
    "\u008D": "",    # Control character
    "\u008E": "",    # Control character
    "\u008F": "",    # Control character
    "\u0090": "",    # Control character
    "\u0091": "",    # Control character
    "\u0092": "",    # Control character
    "\u0093": "",    # Control character
    "\u0094": "",    # Control character
    "\u0095": "",    # Control character
    "\u0096": "",    # Control character
    "\u0097": "",    # Control character
    "\u0098": "",    # Control character
    "\u0099": "",    # Control character
    "\u009A": "",    # Control character
    "\u009B": "",    # Control character
    "\u009C": "",    # Control character
    "\u009D": "",    # Control character
    "\u009E": "",    # Control character
    "\u009F": "",    # Control character
}

# Helper functions
def convert_inpage_text(text: str) -> str:
    """
    Convert InPage encoded text to proper Unicode.
    
    Args:
        text (str): The InPage encoded text
        
    Returns:
        str: Converted Unicode text
    """
    if not text:
        return ""
    
    result = ""
    for char in text:
        # Use mapping if available, otherwise keep original character
        converted_char = inpage_to_unicode.get(char, char)
        result += converted_char
    
    return result

def analyze_text(text: str, max_chars: int = 50) -> dict:
    """
    Analyze text to show character mappings and statistics.
    
    Args:
        text (str): Text to analyze
        max_chars (int): Maximum number of unique characters to analyze in detail
        
    Returns:
        dict: Analysis results
    """
    if not text:
        return {"error": "No text provided"}
    
    char_analysis = {}
    mapped_count = 0
    unmapped_count = 0
    unique_chars = set(text)
    
    for char in unique_chars:
        char_code = f"\\u{ord(char):04X}"
        is_mapped = char in inpage_to_unicode
        count = text.count(char)
        
        char_analysis[char_code] = {
            "character": char,
            "mapped": is_mapped,
            "unicode_equivalent": inpage_to_unicode.get(char, char),
            "count": count
        }
        
        if is_mapped:
            mapped_count += count
        else:
            unmapped_count += count
    
    # Sort by frequency and limit results
    sorted_analysis = dict(sorted(
        char_analysis.items(), 
        key=lambda x: x[1]["count"], 
        reverse=True
    )[:max_chars])
    
    return {
        "total_characters": len(text),
        "unique_characters": len(unique_chars),
        "mapped_characters": mapped_count,
        "unmapped_characters": unmapped_count,
        "mapping_coverage": f"{(mapped_count / len(text)) * 100:.1f}%" if text else "0%",
        "character_analysis": sorted_analysis
    }

def get_unmapped_chars(text: str) -> list:
    """
    Get a list of characters that don't have mappings.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        list: List of unmapped characters with their Unicode codes
    """
    if not text:
        return []
    
    unmapped = []
    unique_chars = set(text)
    
    for char in unique_chars:
        if char not in inpage_to_unicode:
            unmapped.append({
                "character": char,
                "unicode_code": f"\\u{ord(char):04X}",
                "frequency": text.count(char)
            })
    
    # Sort by frequency
    return sorted(unmapped, key=lambda x: x["frequency"], reverse=True)

def test_conversion(sample_text: str = None) -> dict:
    """
    Test the conversion function with sample text.
    
    Args:
        sample_text (str): Optional sample text to test
        
    Returns:
        dict: Test results
    """
    if sample_text is None:
        # Default test with some common InPage characters
        sample_text = "\u00A1\u00B1\u00BD\u00BE" # Should convert to: اسلم
    
    original = sample_text
    converted = convert_inpage_text(sample_text)
    analysis = analyze_text(sample_text)
    
    return {
        "original_text": original,
        "converted_text": converted,
        "analysis": analysis,
        "conversion_successful": len(converted) > 0
    }

# Export main mapping for backward compatibility
__all__ = ['inpage_to_unicode', 'convert_inpage_text', 'analyze_text', 'get_unmapped_chars', 'test_conversion']