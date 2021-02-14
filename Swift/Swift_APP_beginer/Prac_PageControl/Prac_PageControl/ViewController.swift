//
//  ViewController.swift
//  Prac_PageControl
//
//  Created by Seonguk Lee on 2021/02/08.
//

import UIKit



class ViewController: UIViewController {
    @IBOutlet var lblPage: UILabel!
    @IBOutlet var pageControl: UIPageControl!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        pageControl.numberOfPages = 10
        pageControl.currentPage = 1
        lblPage.text = String(pageControl.currentPage)

    }

    @IBAction func changeView(_ sender: UIPageControl) {
        lblPage.text = String(pageControl.currentPage + 1)
    }
    
}

