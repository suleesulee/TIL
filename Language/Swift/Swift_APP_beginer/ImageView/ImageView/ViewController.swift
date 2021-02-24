//
//  ViewController.swift
//  ImageView
//
//  Created by Seonguk Lee on 2021/02/02.
//

import UIKit

class ViewController: UIViewController {
    var isZoom = false
    var img1: UIImage?
    var img2: UIImage?
    
    
    @IBOutlet var imgView: UIImageView!
    @IBOutlet var btnResize: UIButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        img1 = UIImage(named: "lamp1.png")
        img2 = UIImage(named: "R1280x0.jpg")
        
        imgView.image = img1
    }

    @IBAction func btnResizeImage(_ sender: UIButton) {
        let scale: CGFloat = 2.0
        var newWidth:CGFloat, newHeight:CGFloat
        
        if(isZoom) {
            newWidth = imgView.frame.width/scale
            newHeight = imgView.frame.height/scale
            btnResize.setTitle("확대", for: .normal)
        }
        else{
            newWidth = imgView.frame.width*scale
            newHeight = imgView.frame.height*scale
            btnResize.setTitle("축소", for: .normal)
        }
        imgView.frame.size = CGSize(width: newWidth, height: newHeight)
        isZoom = !isZoom
    }
    @IBAction func switchImageChange(_ sender: UISwitch) {
        if sender.isOn{
            imgView.image = img1
        } else {
            imgView.image = img2
        }
    }
    
}


