from unittest.mock import MagicMock, patch
import pytest
from bs4 import BeautifulSoup
import requests
from idt_scrapper.infrastructure.scanners.beautiful_soup_affiliated_link_scanner import BeautifulSoupAffiliatedLinkScanner
from idt_scrapper.domain.errors.scanning_error import ScanningError
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from tests.shared.builders.content_builder import ContentBuilder

@pytest.fixture
def affiliated_link_scanner():
    scanner = BeautifulSoupAffiliatedLinkScanner()
    return scanner

@pytest.mark.parametrize("prompt, expected_link", [
    ("Check this out: https://www.promo.com.", "https://www.promo.com"),
    ("Visit www.example.org for more info", "www.example.org"),
    ("Http links: http://a.com.", "http://a.com"),
])
def test_get_links_should_return_correct_link(affiliated_link_scanner, prompt, expected_link):
    # Act
    result = affiliated_link_scanner.get_links(prompt)
    print(result)
    # Assert
    assert len(result) == 1
    assert result[0] == expected_link

def test_get_links_when_sentence_has_multiple_links_should_return_correct_links(affiliated_link_scanner):
    # Arrange
    expected_links = ['https://www.promo.com', 'https://www.promo2.com']
    prompt = f'This is a description with a link: {expected_links[0]} and another link: {expected_links[1]}'

    # Act
    result = affiliated_link_scanner.get_links(prompt)
    
    # Assert
    assert len(result) == 2
    assert result == expected_links

def test_get_links_when_sentence_has_no_links_should_return_empty_array(affiliated_link_scanner):
    # Arrange
    prompt = f'This is a description without links.'

    # Act
    result = affiliated_link_scanner.get_links(prompt)
    
    # Assert
    assert len(result) == 0
    assert result == []

def test_filter_social_media_links_should_filter_social_media(affiliated_link_scanner):
    # Arrange
    links = ['https://www.instagram.com/test', 'https://www.promo.com']
    expected_links = ['https://www.promo.com']

    # Act
    result = affiliated_link_scanner.filter_social_media_links(links)

    # Assert
    assert len(result) == 1
    assert result == expected_links

def test_filter_social_media_links_should_filter_social_media(affiliated_link_scanner):
    # Arrange
    links = ['https://www.instagram.com/test', 'https://www.promo.com']
    expected_links = ['https://www.promo.com']

    # Act
    result = affiliated_link_scanner.filter_social_media_links(links)
    
    # Assert
    assert len(result) == 1
    assert result == expected_links

def test_get_promo_webpage_should_return_soup(affiliated_link_scanner):
    # Arrange
    link = 'https://dometrain.com'
    response = requests.get(link)
    expected_result = BeautifulSoup(response.content, 'html.parser')
    
    # Act
    result = affiliated_link_scanner.get_promo_webpage(link)
    
    # Assert
    assert result == expected_result

def test_get_promo_webpage_when_link_is_not_ok_should_raise_scanning_error(affiliated_link_scanner):
    # Arrange
    link = 'https://dometrain.com/nonexistent'

    # Act & Assert
    with pytest.raises(ScanningError):
        affiliated_link_scanner.get_promo_webpage(link)

def test_get_top_words_should_return_top_10_ost_common_words(affiliated_link_scanner):
    # Arrange
    link = 'https://dometrain.com'
    response = requests.get(link)
    webpage = BeautifulSoup(response.content, 'html.parser')
    expected_results = ['courses', 'learn']
    
    # Act
    result = affiliated_link_scanner.get_top_words(webpage)

    # Assert
    assert expected_results[0] in result
    assert expected_results[1] in result

def test_get_meta_tags_should_return_all_meta_tags(affiliated_link_scanner):
    # Arrange
    link = 'https://dometrain.com'
    response = requests.get(link)
    webpage = BeautifulSoup(response.content, 'html.parser')
    expected_results = ['Dometrain provides high quality courses, crafted by real engineers, for the real world.']
    
    # Act
    result = affiliated_link_scanner.get_meta_tags(webpage)
    print(result)
    # Assert
    assert expected_results[0] in result

def test_scan_links_return_links(affiliated_link_scanner):
    # Arrange
    mock_content = ContentBuilder().build()
    
    mock_links = ["https://example.com"]
    mock_filtered_links = ["https://example.com"]
    mock_webpage = MagicMock()
    mock_tokens = ["example", "test"]
    mock_meta_tags = ["meta description"]

    with patch.object(affiliated_link_scanner, 'get_links', return_value=mock_links) as mock_get_links, \
        patch.object(affiliated_link_scanner, 'filter_social_media_links', return_value=mock_filtered_links) as mock_filter_links, \
        patch.object(affiliated_link_scanner, 'get_promo_webpage', return_value=mock_webpage) as mock_get_webpage, \
        patch.object(affiliated_link_scanner, 'get_top_words', return_value=mock_tokens) as mock_get_top_words, \
        patch.object(affiliated_link_scanner, 'get_meta_tags', return_value=mock_meta_tags) as mock_get_meta_tags:
        
        # Act
        result = affiliated_link_scanner.scan_links([mock_content])

        # Assert
        assert len(result) == 1
        assert isinstance(result[0], AffiliatedLink)
        assert result[0].link == "https://example.com"
        assert result[0].tokens == mock_tokens + mock_meta_tags
        assert result[0].prompt == mock_content.prompt

        mock_get_links.assert_called_once_with(mock_content.prompt)
        mock_filter_links.assert_called_once_with(mock_links)
        mock_get_webpage.assert_called_once_with("https://example.com")
        mock_get_top_words.assert_called_once_with(mock_webpage)
        mock_get_meta_tags.assert_called_once_with(mock_webpage)